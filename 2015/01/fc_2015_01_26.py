#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.script import Shell, Manager
from flask.ext.restful import Api, reqparse, Resource

#
# Free Coding session for 2015-01-26
# Written by Matt Warren
#


app = Flask(__name__)
api = Api(app)
manager = Manager(app)

parser = reqparse.RequestParser()
parser.add_argument('val', type=str)


class Echo(Resource):
    def get(self):
        args = parser.parse_args()
        return args

api.add_resource(Echo, '/')


def make_shell_context():
    return dict(app=app, api=api, Echo=Echo)
manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
