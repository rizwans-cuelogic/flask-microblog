from app import db,lm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(64),index=True,unique=True)
	email = db.Column(db.String(120),index=True,unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __str__(self):
		return '<USER %s>' %(self.username)

	@property
	def password(self):
		raise AttributeError("Password is not readable attribute")

	@password.setter
	def password(self,password):
		self.password_hash=generate_password_hash(password)

	def verify_password(self,password):
		return check_password_hash(self.password_hash,password)

@lm.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id= db.Column(db.Integer,db.ForeignKey('user.id'))

	def __str__(self):
		return '<Post %s>' %(self.body)