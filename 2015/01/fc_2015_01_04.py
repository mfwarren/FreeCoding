#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.restful import Api, reqparse, abort, Resource
from flask.ext.script import Manager, Shell

#
# Free Coding session for 2015-01-04
# Written by Matt Warren
#

app = Flask(__name__)
api = Api(app)
manager = Manager(app)


parser = reqparse.RequestParser()
parser.add_argument('type', type=str)
parser.add_argument('amount_cents', type=int)

DATA = {1: {'amount': 1.0}}

def abort_if_not_present(t_id):
    if t_id not in DATA:
        abort(404, message='Transfer not found')


class Transfer(Resource):
    def get(self, t_id):
        abort_if_not_present(t_id)
        return DATA[t_id]


class TransferList(Resource):
    def post(self):
        args = parser.parse_args()
        DATA[len(DATA)+1] = args

    def get(self):
        return DATA

api.add_resource(Transfer, '/transfers/<string:t_id>')
api.add_resource(TransferList, '/transfers')

def make_shell_context():
    return dict(app=app, TransferList=TransferList, Transfer=Transfer, api=api)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
