import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'ASDNVOAIWNEVO'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'dev.sqlite'))


config = {
    'default': DevelopmentConfig
}
