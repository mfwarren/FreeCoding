#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.restful import Api, reqparse, Resource
from flask.ext.script import Manager
from fc_2015_01_07 import read_spreadsheet

#
# Free Coding session for 2015-01-09
# Written by Matt Warren
#

app = Flask(__name__)
api = Api(app)
manager = Manager(app)


parser = reqparse.RequestParser()
parser.add_argument('spreadsheet', type=str)


class Spreadsheet(Resource):
    def get(self, name):
        return read_spreadsheet(name)

api.add_resource(Spreadsheet, '/<string:name>')

if __name__ == '__main__':
    manager.run()
