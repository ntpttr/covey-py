# covey/model/user_group.py


from extensions import db


class UserGroup(db.Model):

    __tablename__ = "user_groups"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    is_favorite = db.Column(db.Boolean, nullable=False)

    def __init__(self, is_favorite=False):
        self.is_favorite = is_favorite
