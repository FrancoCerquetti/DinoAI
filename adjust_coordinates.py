import keyboard
import mss
from matplotlib import pyplot as plt
import numpy as np
import cv2
import time
import coordinates

FACTOR = 10

coord = coordinates.coord

sct = mss.mss()

def increment(key):
    coord[key] += FACTOR
    print(coord)

def decrement(key):
    coord[key] -= FACTOR
    print(coord)

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
        
    time.sleep(0.1)