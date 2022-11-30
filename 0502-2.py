#0502-2.py
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while True:
    retval, frame = cap.read()
    if not retval:
        break

    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    dst1 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 2001, 7)
    # dst1 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 401, 7)
    dst2 = 255 - dst1

    src1 = cv2.bitwise_and(frame, frame, mask=dst2)

    cv2.imshow('frame', frame)
    cv2.imshow('dst', src1)

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()
