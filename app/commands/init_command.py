from datetime import datetime
from flask_script import Command
from app.create_app import app, db
from app.user_app.models import User, Role


class InitDbCommand(Command):
    """ Initialize the database."""

    def run(self):
        init_db()   


def init_db():
    """ Initialize the database."""
    db.drop_all()
    db.create_all()
    create_users()


def find_or_create_role(name, desc):
    """ Find existing role or create new role """
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(name=name, desc=desc)
        return role
    return role


def find_or_create_user(username, email, password, role=None):
    """ Find existing user or create new user """
    user = User.query.filter(User.username == username).first()
    if not user:
        user = User(username=username,
                    email=email,
                    email_confirmed_at=datetime.utcnow())
        user.create_password(password)
        if role:
            user.roles.append(role)
        return user
    return user


def create_users():
    """ Create users """

    # Create all tables
    db.create_all()

    # Adding roles
    admin_role = find_or_create_role('admin', u'Admin Role')

    # Add users
    admin_user = find_or_create_user(
        u'admin', u'admin@example.com', 'admin212', admin_role)

    # Save to DB
    admin_user.save()
