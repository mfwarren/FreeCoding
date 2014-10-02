#!/usr/bin/env python
#imports go here
import json
import os
import re

from boto.s3.connection import S3Connection
from boto.s3.cors import CORSConfiguration
import inquirer

#
# Free Coding session for 2014-10-01
# Written by Matt Warren
#
# Load a CORS configuration to allow uploads into a S3 bucket

questions = [
    inquirer.Text('bucket_name',
        message='Bucket Name',
        validate=lambda _, x: re.match('[a-z0-9]+', x),
        ),
    inquirer.Text('hostname',
        message='Allow Access from host:',
        default="*"
        )
]

def load_CORS(bucket, host):
    cors_cfg = CORSConfiguration()
    cors_cfg.add_rule(['PUT', 'POST', 'GET'], host, allowed_header='*', max_age_seconds=3000)
    bucket.set_cors(cors_cfg)

if __name__=='__main__':

    s3 = S3Connection()  #uses environment variables for keys

    answers = inquirer.prompt(questions)

    bucket = s3.lookup(answers['bucket_name'])

    load_CORS(bucket, answers['hostname'])
