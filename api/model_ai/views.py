from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import time
import numpy as np
from tensorflow.keras.models import load_model
import os
from .models import User


camera_on = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model_ai\model", "20240619-model.h5")
CLASSIFIER_PATH = os.path.join(
    BASE_DIR, "model_ai\\utils", "haarcascade_frontalface_default.xml"
)

# Load the face recognition model
model = load_model(MODEL_PATH)
face_cascade = cv2.CascadeClassifier(CLASSIFIER_PATH)


camera_on = True


def draw_ped(
    img, label, x0, y0, xt, yt, color=(0, 107, 214), text_color=(255, 255, 255)
):

    (w, h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(img, (x0, y0 + baseline), (max(xt, x0 + w), yt), color, 2)
    cv2.rectangle(img, (x0, y0 - h), (x0 + w, y0 + baseline), color, -1)
    cv2.putText(
        img, label, (x0, y0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, text_color, 1, cv2.LINE_AA
    )
    return img


def generate_frames():

    global camera_on
    cap = cv2.VideoCapture(0)
    users = list(User.objects.all())

    while camera_on:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            # Chuyển đổi ảnh từ RGB sang Grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        for x, y, w, h in faces:

            face_img = gray[y : y + h, x : x + w]
            face_img = cv2.resize(face_img, (50, 50))
            face_img = face_img.reshape(1, 50, 50, 1)

            result = model.predict(face_img)
            idx = result.argmax(axis=1)
            confidence = result.max(axis=1) * 100

            if isinstance(idx, np.ndarray):
                idx = idx[0]

            if confidence > 80:
                label_text = "%s (%.2f %%)" % (users[idx], confidence)
            else:
                label_text = "N/A"
            frame = draw_ped(
                frame,
                label_text,
                x,
                y,
                x + w,
                y + h,
                color=(0, 255, 255),
                text_color=(50, 50, 50),
            )

            ret, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
            )
            time.sleep(0.1)  # Thời gian delay giữa các frame

    cap.release()


def video_feed(request):
    global camera_on
    if camera_on:
        return StreamingHttpResponse(
            generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame"
        )
    else:
        return JsonResponse({"error": "Camera is off"}, status=400)


@csrf_exempt
def toggle_camera(request):
    global camera_on
    if request.method == "POST":
        camera_on = not camera_on
        return JsonResponse({"camera_on": camera_on})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
