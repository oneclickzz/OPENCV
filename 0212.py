#0212.py

import cv2
from matplotlib import pyplot as plt
import matplotlib.animation as animation

cap = cv2.VideoCapture(0)
fig = plt.figure(figsize=(10,6))

# 윈도우타이틀
fig.canvas.manager.set_window_title('Video Capture')
plt.axis('off')

# im = None

def init():
    global im
    retval, frame = cap.read()
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

def updateFrame(k):
    # print('updateFrame: k: ', k)
    global im
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


# 30fps = 1/30, 60fps = 1/60, 120fps = 1/120, 144fps = 1/144
ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval=6)

plt.show()

if cap.isOpened():
    cap.release()
