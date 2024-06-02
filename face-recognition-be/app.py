from flask import Flask, render_template, Response
import cv2
import numpy as np
from utils.face_recognition import load_model, recognize_faces
from sqlalchemy.orm import scoped_session
from database.initialize import Initialize
from config.default import (
    MYSQL_CONN_STRING
)
from flask_cors import CORS

model = load_model('model/model-cnn-facerecognition.h5')

db = Initialize(MYSQL_CONN_STRING)

app = Flask(__name__)
CORS(app)

db_session = scoped_session(db.SessionLocal)

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    cap = cv2.VideoCapture(0)  # Sử dụng webcam
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Nhận dạng khuôn mặt
            frame = recognize_faces(frame, model)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)