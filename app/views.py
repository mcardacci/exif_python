from flask import render_template, request
from app import app
import exifread
import newspaper


@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html",
                           title='Home',
                           )

@app.route('/profile', methods=['POST'])
def get_photo_data():
    print request.form
    return render_template('profile.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
	# form=LoginForm()
	# if form.validate_on_submit():
	# 	flash('Login')
	# return render_template('login.html',
	# 	title='Sign In',
	# 	form=form)
