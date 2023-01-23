from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config
from config import DATABASE_CONNECTION_URI, SECRET_KEY

# Database
from database.db import db

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

db.init_app(app)
with app.app_context():
  db.create_all()


if __name__ == '__main__':
  app.run(debug=True)