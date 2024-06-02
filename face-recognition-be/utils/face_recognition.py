import cv2
import numpy as np
from keras.models import load_model as keras_load_model

def load_model(model_path):
    model = keras_load_model(model_path)
    return model

def draw_ped(img, label, x0, y0, xt, yt, color=(255,127,0), text_color=(255,255,255)):

    (w, h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(img,
                  (x0, y0 + baseline),  
                  (max(xt, x0 + w), yt), 
                  color, 
                  2)
    cv2.rectangle(img,
                  (x0, y0 - h),  
                  (x0 + w, y0 + baseline), 
                  color, 
                  -1)  
    cv2.putText(img, 
                label, 
                (x0, y0),                   
                cv2.FONT_HERSHEY_SIMPLEX,     
                0.5,                          
                text_color,                
                1,
                cv2.LINE_AA) 
    return img

def recognize_faces(frame, model):
    # Tiền xử lý hình ảnh và nhận dạng khuôn mặt
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (50, 50))
        face_img = face_img.reshape(1, 50, 50, 1)

        result = model.predict(face_img)
        idx = result.argmax(axis=1)[0]
        confidence = result.max(axis=1)[0] * 100
        if confidence > 80:
            # label_text = "%s (%.2f%%)" % (labels[idx], confidence)
            label_text = "%s (%.2f%%)"
        else:
            label_text = "N/A"
        frame = draw_ped(frame, label_text, x, y, x + w, y + h, color=(0, 255, 255), text_color=(50, 50, 50))
    
    return frame

def detect_faces(img):
  face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')
  face_resized = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
  
  return face_resized