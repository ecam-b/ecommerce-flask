from flask import Blueprint, request, jsonify
# Models 
from models.UsuarioModel import UsuarioModel
# Database
from database.db import db


usuario = Blueprint('usuario', __name__)


@usuario.route('/')
def get_usuarios():
  try:
    usuarios = UsuarioModel.query.all()
    list = []
    for usuario in usuarios:
      list.append({
        "id_usuario": usuario.id_usuario,
        "nombregit": usuario.nombregit
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'message': str(ex)})
