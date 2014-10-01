#!/usr/bin/env python
import os
import re

import boto
from boto.s3.connection import S3Connection
from boto.iam.connection import IAMConnection
import inquirer

key_policy_json = """{
  "Statement": [
    {
      "Action": "iam:*AccessKey*",
      "Effect": "Allow",
      "Resource": "%s"
    }
  ]
}"""

bucket_policy_json = """{
  "Statement": [
    {
    "Effect": "Allow",
    "Action": %s,
    "Resource": [
      "arn:aws:s3:::%s",
      "arn:aws:s3:::%s/*"
    ]
  },
  {
    "Effect": "Deny",
    "Action": ["s3:*"],
    "NotResource": [
      "arn:aws:s3:::%s",
      "arn:aws:s3:::%s/*"
    ]
  }]}"""

questions = [
  inquirer.List ('org',
    message='Choose Organization -- have <org>_AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY defined.',
    choices=["COMPANY1", "COMPANY2"]
    ),
  inquirer.Text('bucket_name',
    message='Bucket Name',
    validate=lambda _, x: re.match('[a-z0-9]+', x),
    ),
  inquirer.Text('username',
    message='Username',
    validate=lambda _, value: re.match('[a-z0-9]+', value),
    ),
  inquirer.List('acl',
    message='Choose ACL Policy for user on bucket',
    choices=['read', 'all']
    )
  ]


def s3_bucket_maker( answers ):
    access_key = os.environ[answers['org'] + '_ACCESS_KEY_ID']
    secret_key = os.environ[answers['org'] + '_SECRET_ACCESS_KEY']
    s3conn = S3Connection(access_key, secret_key)
    iamconn = IAMConnection(access_key, secret_key)

    bucket = s3conn.lookup(answers['bucket_name'])
    if bucket:
        print 'bucket (%s) already exists' % answers['bucket_name']
    else:
        try:
            bucket = s3conn.create_bucket(answers['bucket_name'])
        except boto.exception.S3CreateError, e:
            print 'Bucket (%s) is owned by another user' % answers['bucket_name']
            raise e


    user = None
    try:
        user = iamconn.get_user(answers['username'])
    except boto.exception.BotoServerError, e:
        if e.status == 404:
            print 'User not found... creating one'
            user = iamconn.create_user(answers['username'])
            keys = iamconn.create_access_key(answers['username'])
            print keys
        else :
            raise e
    print user

    policy = key_policy_json % (user.arn)
    user_policy = iamconn.put_user_policy(answers['username'], 'UserKeyPolicy', policy)

    actions = "[\"s3:*\"]"
    if (answers['acl'] == 'read'):
        actions = "[\"s3:ListBucket\",\"s3:GetObject\",\"s3:GetObjectVersion\"]"
    policy = bucket_policy_json % (actions, answers['bucket_name'], answers['bucket_name'], answers['bucket_name'], answers['bucket_name'])
    bucket_policy = iamconn.put_user_policy(answers['username'], 'UserS3Policy', policy)


if __name__=='__main__':

    answers = inquirer.prompt(questions)
    s3_bucket_maker(answers)
