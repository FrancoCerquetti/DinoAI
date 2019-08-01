import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Activation, Dropout
from sklearn.model_selection import train_test_split
import mss
import cv2
import keyboard
import time
from matplotlib import pyplot as plt

model = load_model('./model/train.h5')
sct = mss.mss()

coord = {
    "top": 250,
    "left": 600,
    "width": 300,
    "height": 150
}

def take_shot():
    shot = sct.grab(coord)
    shot = np.array(shot)
    
    img = cv2.cvtColor(shot, cv2.COLOR_RGB2GRAY)
    img_resized = cv2.resize(img, (85, 85))
    return img_resized.reshape(1, 85, 85, 1)

def jump():
    print('JUMPING')
    keyboard.press_and_release('up')

def idle():
    print('IDLE')

while True:
    data = take_shot()
    result = model.predict(data)
    prediction = result[0][0]
    
    jump() if prediction > 0.50 else idle()
    
    time.sleep(0.1)