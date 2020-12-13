from app import app
from flask import request,redirect,url_for,render_template,flash,get_flashed_messages,flash,jsonify
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.urls import url_parse
from wtforms.validators import ValidationError
from datetime import datetime


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