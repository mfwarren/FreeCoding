#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.restful import Api, reqparse, abort, Resource

#
# Free Coding session for 2015-04-01
# Written by Matt Warren
#


app = Flask(__name__)
api = Api(app)

TOP_FIVE = ["Launch", "Get Leads", "Build Products", "Signup Clients", "Write Content"]


def abort_if_doesnt_exist(item):
    if item not in TOP_FIVE:
        abort(404, message="not found")

parser = reqparse.RequestParser()
parser.add_argument('topfive', type=str)


class TopFiveItem(Resource):
    def get(self, item):
        return TOP_FIVE[item]

    def delete(self, item):
        if item > len(TOP_FIVE):
            abort(404, "not found")
        TOP_FIVE.remove(item)
        return TOP_FIVE, 204


class TopFive(Resource):
    def get(self):
        return TOP_FIVE

    def post(self):
        args = parser.parse_args()
        TOP_FIVE.append(args['topfive'])
        return TOP_FIVE

api.add_resource(TopFive, '/')
api.add_resource(TopFiveItem, '/<int:item>')

if __name__ == '__main__':
    app.run(debug=True)
