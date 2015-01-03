#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.restful import Api, reqparse, abort, Resource

#
# Free Coding session for 2015-01-02
# Written by Matt Warren
#


app = Flask(__name__)
api = Api(app)


DATA = {'todo1': {'task': 'build api'},
        'todo2': {'task': 'launch'},
        'todo3': {'task': 'profit'}}


def abort_if_todo_doesnt_exist(id):
    if id not in DATA:
        abort(404, message="TODO %s doesn't exist" % id)

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return DATA[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del DATA[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task', args['task']}
        DATA[todo_id] = task
        return task, 201


class TodoList(Resource):
    def get(self):
        return DATA

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(DATA) + 1)
        DATA[todo_id] = {'task': args['task']}
        return DATA[todo_id], 201

api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(TodoList, '/todos')


if __name__ == '__main__':
    app.run(debug=True)
