#!/usr/bin/env python3
# imports go here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#
# Free Coding session for 2015-02-19
# Written by Matt Warren
#

engine = create_engine('sqlite://test.sqlite', convert_unicode=True, echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)


class Users(Base):
    __table__ = Base.metadata.tables['users']
    # model is inferred

if __name__ == '__main__':
    from sqlalchemy.orm import scoped_session, sessionmaker
    db_session = scoped_session(sessionmaker(bind=engine))
    for item in db_session.query(Users.id, Users.name):
        print item
