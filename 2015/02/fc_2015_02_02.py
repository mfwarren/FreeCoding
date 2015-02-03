#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-02-02
# Written by Matt Warren
#


class Config(object):
    SETTINGS_KEY = 'asdf'
    MAIL_SERVER = 'mail.server'


class ProductionConfig(Config):
    DEBUG = False


class AppConfig(dict):

    def from_object(self, obj):
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)


if __name__ == '__main__':
    config = AppConfig()
    config.from_object(ProductionConfig())

    print(config['MAIL_SERVER'])
