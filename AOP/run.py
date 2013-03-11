'''
Created on 03/03/2013

@author: Administrador
'''
from app import app
from app.modelo.autenticacion.Usuario import Usuario
from config import init_db, db_session

init_db()

u=Usuario();
u.apellido='a'
u.email='a@gmail.com'
u.nombre='aaa'
u.telefono='aaa'
u.user='ra'

db_session.add(u)

app.run(debug=False)
