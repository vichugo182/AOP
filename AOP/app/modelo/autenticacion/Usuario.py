# -*- coding: utf-8 -*-
'''
Created on 04/03/2013

@author: Administrador
'''
from config import Base
from datetime import datetime
from sqlalchemy import Table, ForeignKey, Column, and_, or_, not_
from sqlalchemy.orm import relation, synonym, relationship
from sqlalchemy.types import Unicode, Integer, DateTime
from config import Base
import os
import sys
try:
    from hashlib import sha1
except ImportError:
    sys.exit('ImportError: No module named hashlib\n'
             'If you are on python2.4 this library is not part of python. '
             'Please install it. Example: easy_install hashlib')


class Usuario(Base):
    """
    User definition.

    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.
    Pero se usa un 'translation' a "nombre_usuario" y "roles"
    """
    __tablename__ = 'usuario'
    _to_serialize = ("id","user","nombre", "email",
            "apellido", "telefono", "nro_documento")

    

    id = Column(Integer, autoincrement=True, primary_key=True)
    user = Column(Unicode(32), unique=True, nullable=False)
    email = Column(Unicode(100), unique=True, nullable=False,
                           info = {'rum': {'field':'Email'}})
    nombre = Column(Unicode(50))
    apellido = Column(Unicode(50))
    telefono = Column(Unicode(15))
    nro_documento = Column(Integer)
    _password = Column('password', Unicode(80),
                       info = {'rum': {'field':'Password'}})
    estado = Column(Unicode(15))
    creado = Column(DateTime, default=datetime.now)
    #roles = relationship('Rol', secondary=user_group_table, backref='Usuario')

    #{ Special methods
    def __repr__(self):
        return ('<User: name=%r, email=%r, display=%r>' % (
                self.user, self.email, self.nombre)).encode('utf-8')

    def __unicode__(self):
        return self.nombre or self.nombre_usuario

