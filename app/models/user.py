# from .. import db
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(256), nullable=False)

from .. import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  full_name = db.Column(db.String(255), unique=True, nullable=False)
  email = db.Column(db.String(50),unique=True, nullable=False)
  phone = db.Column(db.Integer,unique=True, nullable=False)
  password = db.Column(db.String(10),nullable=False)

  def __repr__(self):
    return f'<User: {self.Full_name}>'
  
  def get_id(self):
    return self.id

