from database.db import db

class RolModel(db.Model):
  __tablename__ = 'rol'

  id_rol = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(30))
  descripcion = db.Column(db.String(255))
  estado = db.Column(db.Integer)
  usuarios = db.relationship('UsuarioModel')


  def __init__(self, nombre, description, estado):
    self.nombre = nombre
    self.descripcion = description
    self.estado = estado