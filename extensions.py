from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
cors = CORS()
bcrypt = Bcrypt()
jwt = JWTManager()
admin = Admin(template_mode="bootstrap3")
