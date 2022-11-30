#0501.py
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while True:
    retval, frame = cap.read()
    if not retval:
        break

    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ret, dst = cv2.threshold(dst, 120, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, dst = cv2.threshold(dst, 130, 255, cv2.THRESH_BINARY)
    dst1 = 255 - dst

    src1 = cv2.bitwise_and(frame, frame, mask=dst1)

    cv2.imshow('frame', frame)
    cv2.imshow('dst', src1)

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()