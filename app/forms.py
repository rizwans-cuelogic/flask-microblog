from flask_wtf import Form
from wtforms import StringField,BooleanField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class LoginForm(Form):
	email = StringField('Email',validators=[ DataRequired(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)
	submit= SubmitField("Log In")


