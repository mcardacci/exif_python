from flask import render_template, request
from app import app
import exifread
import newspaper
import ast

@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html",
                           title='Home',
                           )

@app.route('/profile', methods=['POST'])
def get_photo_data():
    dateStamp=request.form.get("dateStamp")
    longitude=request.form.get("longitude")
    latitude=request.form.get("latitude")
    latRef=request.form.get("latRef")
    longRef=request.form.get("longRef")
    
    print dateStamp
    print longitude.split(',')
    print latitude.split(',')
    print latRef 
    print longRef

    return render_template('profile.html', 
    dateStamp=dateStamp, 
    longitude=longitude,
    latitude=latitude,
    latRef=latRef,
    longRef=longRef
    )


# @app.route('/login', methods=['GET', 'POST'])
# def login():
	# form=LoginForm()
	# if form.validate_on_submit():
	# 	flash('Login')
	# return render_template('login.html',
	# 	title='Sign In',
	# 	form=form)
