from flask import render_template,flash,redirect,url_for,request,g,abort
from flask_login import login_user,logout_user,login_required
from app import app
from .forms import LoginForm
from .models import User,Post

@app.route('/')
def index():
	posts = [
			{ 
				'author' : 'Susan',
			  	'body':'Hello, its my birthday today.'	
			},
			{
				'author':'Michelle',
				'body': 'that nice. happy birthday to you.'
			},
			{
				'author':'john',
				'body':'please,dont post such things here.'
			}
		]

	return render_template('index.html',title="Home",posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
	login_form=LoginForm()

	if login_form.validate_on_submit():
		user = User.query.filter_by(email=login_form.email.data).first()
		if user is not None and user.verify_password(login_form.password.data):
			login_user(user,login_form.remember_me.data)
			return redirect(url_for('index'))
		flash("Invalid Username and Password")	
	return render_template('login.html',title='Login',form=login_form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You have been logged out")
	return redirect(url_for('index'))


@app.route('/addpost')
@login_required
def addpost():
	abort(401)
