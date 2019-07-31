import os
import cv2
import random
import numpy as np

def load_data():
    CATEGORIES = ['jump', 'idle']

    images = []

    for category in CATEGORIES:
        for file in os.listdir(f'./{category}'):
            data = cv2.imread(f'./{category}/{file}', cv2.COLOR_BGR2GRAY)
            resized_data = cv2.resize(data, (80, 80))
            label = CATEGORIES.index(category)
            images.append([resized_data, label])

    random.shuffle(images)

    x_train = []
    y_train = []

    for feature, label in images:
        x_train.append(feature)
        y_train.append(label)
        
    x = np.array(x_train).reshape(-1, 80, 80, 1)
    y = np.array(y_train).reshape(-1, 1)

    x = x/255
    
    return (x, y)