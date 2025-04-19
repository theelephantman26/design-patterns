import numpy as np
import cv2 as cv
from pynput import keyboard

img = np.zeros((512, 512, 3), np.uint8)
global_var = None

def rotateLineAroundCenter(img, delta):
    h, w = img.shape[:2]
    cX, cY = w // 2, h // 2
    M = cv.getRotationMatrix2D((cX, cY), -delta, 1.0)
    rotated = cv.warpAffine(img, M, (w, h))
    return rotated

def showRotatingLine(img, delta):
    while True:
        img = rotateLineAroundCenter(img, delta)
        cv.imshow("img", img)
        cv.waitKey(10)

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    
    try:
        k = key.char
    except:
        k = key.name

    if k in ['1', '2', 'left', 'right']:
        global_var = k
    

img = cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# img = rotateLineAroundCenter(img)
# cv.imshow("img", img)

# cv.waitKey(0)

# cv.destroyAllWindows()
listener = keyboard.Listener(on_press=on_press)
listener.start()
showRotatingLine(img, 2)
listener.join()