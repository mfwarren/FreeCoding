#!/usr/bin/env python3
# imports go here
import requests
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#
# Free Coding session for 2015-02-23
# Written by Matt Warren
#

engine = create_engine('sqlite://dbcopy.sqlite', convert_unicode=True, echo=True)
Base = declarative_base()
Base.metadata.reflect(engine)


class Obj(Base):
    __table__ = Base.metadata.tables['objects']
    # model is inferred

if __name__ == '__main__':
    from sqlalchemy.orm import scoped_session, sessionmaker
    db_session = scoped_session(sessionmaker(bind=engine))

    remote_objects = requests.get('http:/server.com/1/classes/Objects').json()

    for obj in remote_objects:
        db_session.add(Obj(obj))
    db_session.commit()
