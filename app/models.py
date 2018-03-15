from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from app import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(64),unique=True)
#
#     def __repr__(self):
#         return '<Role %r>' % self.name


class User(UserMixin,db.Model):
    __tablename__ = 'tb_Users'
    UserId = db.Column(db.String(32),unique=True,primary_key = True,index=True)
    UserName = db.Column(db.String(12),unique=True)
    Sex = db.Column(db.Boolean)
    Password_hash = db.Column(db.String(128))
    Level = db.Column(db.Integer)
    Truename = db.Column(db.String(64))
    Email = db.Column(db.String(64),unique=True)
    PhoneCode = db.Column(db.String(16),unique=True)
    City = db.Column(db.String(64))
    Address = db.Column(db.String(64))
    PostCode = db.Column(db.String(8))
    LastDate = db.Column(db.DateTime)
    RedDate = db.Column(db.DateTime)
    Point = db.Column(db.Integer)

    # __tablename__ = 'users'
    # id = db.Column(db.Integer,primary_key=True)
    # email = db.Column(db.String(64),unique=True,index=True)
    # username=db.Column(db.String(64),unique=True,index=True)
    # password_hash = db.Column(db.String(128))


    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a')
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User %r>' % self.username
