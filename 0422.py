# 0422.py
import cv2
import numpy as np
import time

nPoints = 100
pts = np.zeros((1, nPoints, 2), dtype=np.uint16)

while True:

    dst = np.full((512,512,3), (255,255,255), dtype = np.uint8)

    cv2.setRNGSeed(int(time.time()))
    cv2.randu(pts, (256, 256), (50, 50))

    for k in range(nPoints):
        x,y = pts[0, k][:]   #pts[0,k,:]
        cv2.circle(dst, (x,y), radius=5, color=(0,0,255), thickness=-1)

    cv2.imshow('dst', dst)
    key = cv2.waitKey()
    if key == 27:
        break