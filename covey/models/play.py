# covey/model/play.py


from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSON

from extensions import db


class Play(db.Model):

    __tablename__ = "plays"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    winner = db.Column(db.String(128))
    scores = db.Column(JSON)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, name=""):
        self.name = name
