from flask import Flask, render_template, Response
from camera import VideoCamera
from flask import Flask, request,render_template,url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = '../upload_files'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
