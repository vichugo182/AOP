#!/usr/local/bin/python2.7
# encoding: utf-8
'''
config -- shortdesc

config is a description

It defines classes_and_methods

@author:     user_name
        
@copyright:  2013 organization_name. All rights reserved.
        
@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from flask.app import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import sys


# conexion a la base de datso
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/dbaop'

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.modelo.autenticacion
    Base.metadata.create_all(bind=engine)