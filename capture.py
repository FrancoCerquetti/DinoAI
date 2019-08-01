import cv2
import mss
import numpy as np
import keyboard
from matplotlib import pyplot as plt
import time
import sys
import random
import coordinates

sct = mss.mss()

coord = coordinates.coord

JUMP_PATH = "jump/"
IDLE_PATH = "idle/"

jump = 0
idle = 0

while True:

    shot = np.array(sct.grab(coord))

    if keyboard.is_pressed('q'):
        break

    if keyboard.is_pressed('up') and ('jump' in sys.argv):
        print(f'Saving jump')
        img =  cv2.cvtColor(shot, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{JUMP_PATH}jump_{random.randrange(1000)}.jpg', img)
        time.sleep(0.8)
        

    if keyboard.is_pressed('i') and ('idle' in sys.argv):
        print(f'Saving idle')
        img =  cv2.cvtColor(shot, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'{IDLE_PATH}idle_{random.randrange(1000)}.jpg', img)
        time.sleep(0.8)

    if keyboard.is_pressed('q'):
        break

