from hashlib import md5, sha256
from flask import current_app as app
from flask_user import UserMixin

from app.create_app import db


# Define the User data Model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, default='')

    # User Email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())

    # User information
    is_enabled = db.Column(db.Boolean(), nullable=False, default=True)
    trash = db.Column(db.Boolean, nullable=False, default=False)
    roles = db.relationship(
        'Role',
        secondary='users_roles'
    )

    def is_active(self):
        return self.is_enabled

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    def remove(self):
        self.trash = True
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def restore(self):
        self.trash = False
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_username(username):
        return User.query.filter(
            User.username == username).first()

    def create_password(self, password):
        self.password = str(
            sha256(
                str(
                    md5(str(password).encode('utf-8')).hexdigest()
                ).encode('utf-8')
            ).hexdigest()
        )

    def check_password(self, password):
        return self.password == str(
            sha256(
                str(
                    md5(str(password).encode('utf-8')).hexdigest()
                ).encode('utf-8')
            ).hexdigest()
        )


# Define the Role data model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(
        db.String(50),
        nullable=False,
        server_default=u'',
        unique=True)  # for @roles_accepted()
    desc = db.Column(db.Text)  # for display purposes

    def save(self):
        db.session.add(self)
        db.session.commit()


# Define the UserRoles association model
class UsersRoles(db.Model):
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id', ondelete='CASCADE'))
