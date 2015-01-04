#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.restful import Api, reqparse, abort, Resource
from flask.ext.script import Shell, Manager

#
# Free Coding session for 2015-01-03
# Written by Matt Warren
#

DATA = {'todo1': {'task': "somethink"},
        'todo2': {'task': 'launch'},
        'todo3': {'task': 'profit'}}

app = Flask(__name__)
api = Api(app)
manager = Manager(app)


def abort_if_not_there(todo_id):
    if todo_id not in DATA:
        abort(404, message='not found')


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Todo(Resource):
    def get(self, todo_id):
        abort_if_not_there(todo_id)
        return DATA[todo_id]

    def delete(self, todo_id):
        abort_if_not_there(todo_id)
        del DATA[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        DATA[todo_id] = {'task': args['task']}
        return DATA[todo_id], 201


class TodoList(Resource):
    def get(self):
        return DATA

    def post(self):
        args = parser.parse_args()
        DATA['todo%d' % (len(DATA) + 1)] = {'task', args['task']}
        return {'task', args['task']}, 201

api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(TodoList, '/todos')


def make_shell_context():
    return dict(Todo=Todo, TodoList=TodoList, app=app, api=api)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
