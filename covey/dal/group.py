# covey/dal/groups.py


from extensions import db
from covey.models.group import Group


def get_all_groups():
    return Group.query.all()


def get_group_by_id(group_id):
    return Group.query.filter_by(id=group_id).first()


def create_group(name, description=""):
    group = Group(name=name, description=description)
    db.session.add(group)
    db.session.commit()
    return group


def update_group(group, name="", description=""):
    group.name = name
    group.description = description
    db.session.commit()
    return group


def delete_group(group):
    db.session.delete(group)
    db.session.commit()
    return group
