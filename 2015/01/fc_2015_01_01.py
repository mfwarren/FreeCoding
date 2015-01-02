#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext import restful


#
# Free Coding session for 2015-01-01
# Written by Matt Warren
#


app = Flask(__name__)
api = restful.Api(app)


class HelloResource(restful.Resource):
    def get(self):
        return {"status": 200}

api.add_resource(HelloResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
