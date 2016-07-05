from flask import render_template, request, redirect
from exify import app
from models import Picture, db
import exifread
#import newspaper
import ast


@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html",
                           title='Home',
                           )

@app.route('/store', methods=['POST'])
def store_photo_data():
    dateStamp=request.form.get("dateStamp")
    lon_list=request.form.get("longitude").split(',')
    lat_list=request.form.get("latitude").split(',')
    longitude=[float(i) for i in lon_list]
    latitude=[float(i) for i in lat_list]
    latRef=request.form.get("latRef")
    longRef=request.form.get("longRef")  
    
    print latRef
    print latitude
    print longRef
    print longitude

    return redirect('/')

    # return render_template('profile.html', 
    # dateStamp=dateStamp, 
    # longitude=longitude,
    # latitude=latitude,
    # latRef=latRef,
    # longRef=longRef
    # )
    
@app.route('/profile', methods=['GET'])
def get_all_photos_from_user():
    pics=Picture.query.all()
    
    return render_template('profile.html',pictures=pics)
    
# @app.route('/login', methods=['GET', 'POST']) # def login():
#	 form=LoginForm()
#	 if form.validate_on_submit():
#	 	flash('Login')
#	 return render_template('login.html',
#	 	title='Sign In',
#	 	form=form)

@app.route('/login', methods=['GET'])
def render_login_page():
    return render_template('login.html')

@app.route('/welcome', methods=['GET'])
def render_welcome_page():
    return render_template('welcome.html')
