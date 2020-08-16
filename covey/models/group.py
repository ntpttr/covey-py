# covey/model/group.py


from sqlalchemy.sql import func

from extensions import db


class Group(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    games = db.relationship("Game", backref="group", lazy=True)
    plays = db.relationship("Play", backref="group", lazy=True)

    def __init__(self, name=""):
        self.name = name
