import keyboard
import mss
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time

FACTOR = 10

coord = {
    'top': 100,
    'left': 100,
    'width': 100,
    'height': 100
}

sct = mss.mss()

def increment(key):
    coord[key] += FACTOR

def decrement(key):
    coord[key] -= FACTOR

while True:
    if keyboard.is_pressed('q'):
        break
    
    if keyboard.is_pressed('enter'):
        img = np.array(sct.grab(coord))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plt.imshow(img)
        plt.show()
        
    if keyboard.is_pressed('1'):
        increment('top')
        
    if keyboard.is_pressed('2'):
        decrement('top')
        
    if keyboard.is_pressed('3'):
        increment('left')
        
    if keyboard.is_pressed('4'):
        decrement('left')
        
    if keyboard.is_pressed('5'):
        increment('width')
        
    if keyboard.is_pressed('6'):
        decrement('width')
        
    if keyboard.is_pressed('7'):
        increment('height')
        
    if keyboard.is_pressed('8'):
        decrement('height')
        
    print(coord)
    time.sleep(0.1)