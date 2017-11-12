from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
def index():
	user = { 'username':'Rizwan'}
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

	return render_template('index.html',title="Home",user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
	login_form=LoginForm()

	return render_template('login.html',title='Login',form=login_form)





