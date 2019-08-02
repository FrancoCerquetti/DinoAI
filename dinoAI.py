import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Activation, Dropout
from sklearn.model_selection import train_test_split
import mss
import cv2
import keyboard
import time
from matplotlib import pyplot as plt
import coordinates

model = load_model('./model/train.h5')
sct = mss.mss()
IMG_SIZE = 100

coord = coordinates.coord

def take_shot():
    shot = sct.grab(coord)
    shot = np.array(shot)
    
    img = cv2.cvtColor(shot, cv2.COLOR_RGB2GRAY)
    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    return img_resized.reshape(1, IMG_SIZE, IMG_SIZE, 1)

def jump():
    print('JUMPING')
    keyboard.press('up')
    time.sleep(0.15)
    keyboard.release('up')

def idle():
    print('IDLE')

while True:
    if keyboard.is_pressed('q'):
        break

    data = take_shot()
    result = model.predict(data)
    prediction = result[0][0]

    jump() if prediction == 1.0 else idle()