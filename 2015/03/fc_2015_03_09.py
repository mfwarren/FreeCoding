#!/usr/bin/env python3
# imports go here
from itsdangerous import Signer, BadSignature, TimestampSigner, SignatureExpired, JSONWebSignatureSerializer
import time

#
# Free Coding session for 2015-03-09
# Written by Matt Warren
#


if __name__ == '__main__':
    s = Signer('secret-password')
    signed_string = s.sign(b'data to sign')
    print(signed_string)  # HMAC SHA1 signed string

    # tamper with string
    signed_string = b'my ' + signed_string
    try:
        s.unsign(signed_string)
    except BadSignature as e:
        print("failed to unsign the modified data")

    s = TimestampSigner('secret-password', salt='signup')  # adds current time to data
    signed_string = s.sign(b'data to sign')
    print(signed_string)
    s.unsign(signed_string, max_age=5)  # would only unsign if signed less than 5 seconds ago
    time.sleep(2)
    try:
        s.unsign(signed_string, max_age=1)  # would only unsign if signed less than 1 seconds ago
    except SignatureExpired as e:
        print('tried to unsign expired data')

    s = JSONWebSignatureSerializer('secret-password')
    print(s.dumps({'name': 'matt'}))
