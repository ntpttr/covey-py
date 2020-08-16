# covey/model/user.py


import datetime

from flask import current_app
from flask_jwt_extended import create_access_token
from sqlalchemy.sql import func

from extensions import db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    # groups = db.relationship("Group", secondary="user_groups", backref="users")

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()

    def encode_token(self):
        seconds = current_app.config.get("ACCESS_TOKEN_EXPIRATION")

        return create_access_token(
            identity=self.username,
            expires_delta=datetime.timedelta(seconds=seconds)
        )
