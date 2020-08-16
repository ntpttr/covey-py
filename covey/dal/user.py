# covey/dal/users.py


from extensions import db
from covey.models.user import User


class UserDAL(object):

    @classmethod
    def get(cls, user_id):
        return User.query.filter_by(id=user_id).first()

    @classmethod
    def get_all():
        return User.query.all()

    @classmethod
    def create(username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    def add_user(username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(user, username, email):
        user.username = username
        user.email = email
        db.session.commit()
        return user

    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
        return user
