import os

if os.path.isfile('.env'):
    for line in open('.env'):
        line = line.strip().split('=')
        if len(line) == 2:
            os.environ[line[0]] = line[1]


from app import create_app, db
from app import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app(os.environ['FLASK_CONFIG'] or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def create_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(create_shell_context))
manager.add_command('migrate', MigrateCommand)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
