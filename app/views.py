from flask import render_template, request
from app import app
import exifread
import newspaper


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Marco'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Eva'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/profile', methods=['POST', 'GET'])
def get_photo_data():
    if request.method=='POST':
        form=request.form
        return render_template('profile.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
	# form=LoginForm()
	# if form.validate_on_submit():
	# 	flash('Login')
	# return render_template('login.html',
	# 	title='Sign In',
	# 	form=form)