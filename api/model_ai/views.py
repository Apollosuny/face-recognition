from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from django.core.files.storage import default_storage
from django.http import StreamingHttpResponse
import cv2
import time
import numpy as np
import tensorflow as tf


class ModelAIView(APIView):
    # def post(self, request, *args, **kwargs):
    #     serializer = ImageUploadSerializer(data=request.data)
    #     if serializer.is_valid():
    #         image = serializer.validated_data["image"]
    #         # Lưu tạm thời ảnh nhận được
    #         temp_image_path = default_storage.save("temp.jpg", image)
    #         temp_image_path = default_storage.path(temp_image_path)

    #         # Đọc ảnh và thực hiện nhận diện khuôn mặt
    #         img = cv2.imread(temp_image_path)
    #         faces = self.detect_faces(img)

    #         # Xóa ảnh tạm thời
    #         default_storage.delete(temp_image_path)

    #         return Response(faces, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def detect_faces(self, img):
    #     # Chuyển ảnh sang định dạng RGB
    #     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #     # Load mô hình nhận diện khuôn mặt
    #     model = tf.keras.models.load_model("./model/model-cnn-facerecognition.h5")

    #     # Tiền xử lý ảnh (resize, normalize, etc.)
    #     input_image = cv2.resize(img_rgb, (224, 224))
    #     input_image = np.expand_dims(input_image, axis=0)

    #     # Dự đoán
    #     predictions = model.predict(input_image)
    #     # Xử lý kết quả
    #     faces = self.process_predictions(predictions)

    #     return faces

    # def process_predictions(self, predictions):
    #     # Giả sử hàm trả về danh sách các khuôn mặt nhận diện được
    #     faces = []
    #     for pred in predictions:
    #         face = {
    #             "label": np.argmax(pred),
    #             "confidence": np.max(pred),
    #         }
    #         faces.append(face)
    #     return faces

    def video_feed(request):
        def generate_frames():
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                else:
                    ret, buffer = cv2.imencode(".jpg", frame)
                    frame_bytes = buffer.tobytes()
                    yield (
                        b"--frame\r\n"
                        b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
                    )
                    time.sleep(0.1)  # Thời gian delay giữa các frame

        return StreamingHttpResponse(
            generate_frames(), content_type="multipart/x-mixed-replace; boundary=frame"
        )
