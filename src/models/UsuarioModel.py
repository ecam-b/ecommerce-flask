from database.db import db

class UsuarioModel(db.Model):
  __tablename__ = 'usuario'

  id_usuario = db.Column(db.Integer, primary_key=True)
  id_rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'))
  nombre = db.Column(db.String(100))
  tipo_documento = db.Column(db.String(20))
  num_documento = db.Column(db.String(20))
  dirrecion = db.Column(db.String(70))
  telefono = db.Column(db.String(20))
  email = db.Column(db.String(50))
  clave = db.Column(db.String(500))
  estado = db.Column(db.Integer)


  def __init__(self, id_rol, nombre, tipo_documento, num_documento, direccion, telefono, email, clave, estado):
    self.id_rol = id_rol
    self.nombre = nombre
    self.tipo_documento = tipo_documento
    self.num_documento = num_documento
    self.dirrecion = direccion
    self.telefono = telefono
    self.email = email
    self.clave = clave
    self.estado = estado