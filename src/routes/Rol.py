from flask import Blueprint, request, jsonify

# Models
from models.RolModel import RolModel
# Database
from database.db import db

rol = Blueprint('rol', __name__)

@rol.route('/')
def get_roles():
  try:
    roles = RolModel.query.all()
    list = []
    for rol in roles:
      list.append({
        "id_rol": rol.id_rol,
        "nombre": rol.nombre
      })
    return jsonify(list)
  except Exception as ex:
    return jsonify({'message': str(ex)})