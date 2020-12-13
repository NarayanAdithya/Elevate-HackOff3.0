from app import app,db
from app.models import User,Patient
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash,jsonify,Response
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.urls import url_parse
from wtforms.validators import ValidationError
from datetime import datetime
from app.camera import VideoCamera
import pandas as pd
import pickle

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    current_user.last_seen=datetime.utcnow()
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))

@app.route('/login',methods=['POST','GET'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method=='POST':
        user=User.query.filter_by(email=request.form['email']).first()
        user.check_password(request.form['password'])
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid Email or Password',category="danger")
            return redirect(url_for('login'))
        login_user(user)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('home')
        return redirect(next_page)
    return render_template('singindoctor.html')



@app.route('/patient',methods=['POST','GET'])
def Patientin():
    if request.method=='POST':
        user_name=request.form['doctorname']
        user_id=request.form['doctorid']
        p=Patient.query.filter_by(patient_key=user_id).first()
        if p is None and p.consults.username!=user_name:
            flash('Invalid id or doctor name',category="danger")
            return redirect(url_for('Patientin'))
        return render_template('patientcheckin.html')
    return render_template('session.html')

@app.route('/contact')
def contact():
    return "hello"

@app.route('/profile')
def profile():
    a=pickle.load(open('app/emotions.pkl','rb'))
    data=pd.DataFrame(a)
    a=data[0].value_counts().to_dict()
    return render_template('profile.html',a=a)



def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
