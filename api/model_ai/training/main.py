# import packages
import os
import cv2
import itertools
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import keras
from keras.models import Sequential, Model

from keras.utils import to_categorical
from keras.layers import (
    ZeroPadding2D,
    Convolution2D,
    MaxPooling2D,
    Conv2D,
    MaxPool2D,
    Flatten,
    Dense,
    Dropout,
    Flatten,
    Activation,
    Input,
    BatchNormalization,
)


def detect_face(img):
    face_cascade = cv2.CascadeClassifier("../utils/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    if len(faces) == 0:
        return None

    # Get the first detection face - can choose random
    x, y, w, h = faces[0]

    # Crop the face from the image
    face = img[y : y + h, x : x + w]

    face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    face_resized = cv2.resize(face_gray, (50, 50))

    return face_resized


def print_progress(val, val_len, folder, bar_size=20):
    progr = "#" * round((val) * bar_size / val_len) + " " * round(
        (val_len - (val)) * bar_size / val_len
    )
    if val == 0:
        print("", end="\n")
    else:
        print(
            "[%s] (%d samples)\t label : %s \t\t" % (progr, val + 1, folder), end="\r"
        )


dataset_folder = "../../../dataset/data/"

names = []
images = []
for folder in os.listdir(dataset_folder):
    files = os.listdir(os.path.join(dataset_folder, folder))[:150]
    if len(files) < 50:
        continue
    for i, name in enumerate(files):
        if name.find(".jpg") > -1:
            img = cv2.imread(os.path.join(dataset_folder + folder, name))
            img = detect_face(img)
            if img is not None:
                images.append(img)
                names.append(folder)

                print_progress(i, len(files), folder)


def img_augmentation(img):
    h, w = img.shape
    center = (w // 2, h // 2)
    M_rot_5 = cv2.getRotationMatrix2D(center, 5, 1.0)
    M_rot_neg_5 = cv2.getRotationMatrix2D(center, -5, 1.0)
    M_rot_10 = cv2.getRotationMatrix2D(center, 10, 1.0)
    M_rot_neg_10 = cv2.getRotationMatrix2D(center, -10, 1.0)
    M_trans_3 = np.float32([[1, 0, 3], [0, 1, 0]])
    M_trans_neg_3 = np.float32([[1, 0, -3], [0, 1, 0]])
    M_trans_6 = np.float32([[1, 0, 6], [0, 1, 0]])
    M_trans_neg_6 = np.float32([[1, 0, -6], [0, 1, 0]])
    M_trans_y3 = np.float32([[1, 0, 0], [0, 1, 3]])
    M_trans_neg_y3 = np.float32([[1, 0, 0], [0, 1, -3]])
    M_trans_y6 = np.float32([[1, 0, 0], [0, 1, 6]])
    M_trans_neg_y6 = np.float32([[1, 0, 0], [0, 1, -6]])

    imgs = []
    imgs.append(cv2.warpAffine(img, M_rot_5, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_rot_neg_5, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_rot_10, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_rot_neg_10, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_trans_3, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_trans_neg_3, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_trans_6, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_trans_neg_6, (w, h), borderValue=(255, 255, 255)))
    imgs.append(cv2.warpAffine(img, M_trans_y3, (w, h), borderValue=(255, 255, 255)))
    imgs.append(
        cv2.warpAffine(img, M_trans_neg_y3, (w, h), borderValue=(255, 255, 255))
    )
    imgs.append(cv2.warpAffine(img, M_trans_y6, (w, h), borderValue=(255, 255, 255)))
    imgs.append(
        cv2.warpAffine(img, M_trans_neg_y6, (w, h), borderValue=(255, 255, 255))
    )
    imgs.append(cv2.add(img, 10))
    imgs.append(cv2.add(img, 30))
    imgs.append(cv2.add(img, -10))
    imgs.append(cv2.add(img, -30))
    imgs.append(cv2.add(img, 15))
    imgs.append(cv2.add(img, 45))
    imgs.append(cv2.add(img, -15))
    imgs.append(cv2.add(img, -45))

    return imgs


augmented_images = []
augmented_names = []
for i, img in enumerate(images):
    try:
        augmented_images.extend(img_augmentation(img))
        augmented_names.extend([names[i]] * 20)
    except:
        print(i)

images.extend(augmented_images)
names.extend(augmented_names)

# reduce sample size per-class using numpy random choice
n = 1000


def randc(labels, l):
    return np.random.choice(np.where(np.array(labels) == l)[0], n, replace=False)


mask = np.hstack([randc(names, l) for l in np.unique(names)])

names = [names[m] for m in mask]
images = [images[m] for m in mask]

le = LabelEncoder()

le.fit(names)

labels = le.classes_

name_vec = le.transform(names)

categorical_name_vec = to_categorical(name_vec)

print(labels)
