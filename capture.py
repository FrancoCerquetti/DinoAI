import cv2
import mss
import numpy as np
import keyboard
from matplotlib import pyplot as plt
import time

sct = mss.mss()

coord = {
    "top": 320,
    "left": 550,
    "width": 500,
    "height": 150
}

JUMP_PATH = "jump/"
IDLE_PATH = "idle/"

jump = 0
idle = 0

while True:

    shot = np.array(sct.grab(coord))

    if keyboard.is_pressed('q'):
        break

    if keyboard.is_pressed('up'):
        print(f'Saving jump {jump}')
        img =  cv2.cvtColor(shot, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{JUMP_PATH}jump_{jump}.jpg', img)
        jump += 1
        time.sleep(0.8)
        

    if keyboard.is_pressed('i'):
        print(f'Saving idle {idle}')
        img =  cv2.cvtColor(shot, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{IDLE_PATH}idle_{idle}.jpg', img)
        idle += 1
        time.sleep(0.8)

    if keyboard.is_pressed('q'):
        break

