#0611.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# src = cv2.imread('./data/T.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('/home/dongkyu/data/alphabet.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.bitwise_not(src)

ret, A1 = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY)
ret, A2 = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY)
skel_dst1 = np.zeros(src.shape, np.uint8)
skel_dst2 = np.zeros(src.shape, np.uint8)

shape1 = cv2.MORPH_CROSS
shape2 = cv2.MORPH_RECT

B1 = cv2.getStructuringElement(shape=shape1, ksize=(3,3))
B2 = cv2.getStructuringElement(shape=shape2, ksize=(3,3))

enable = True
while enable:
    erode = cv2.erode(A1, B1)
    # opening = cv2.dilate(erode, B1)
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, B1)
    # tmp = cv2.absdiff(erode, opening)
    tmp = cv2.subtract(erode, opening)
    skel_dst1 = cv2.bitwise_or(skel_dst1, tmp)
    A1 = erode.copy()
    # done = cv2.countNonZero(A1) != 0  #대상이 비어있으면 false
    enable = cv2.countNonZero(A1) > 0  #대상이 비어있으면 false


enable = True
while enable:
    erode = cv2.erode(A2, B2)
    # opening = cv2.dilate(erode, B2)
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, B2)
    # tmp = cv2.absdiff(erode, opening)
    tmp = cv2.subtract(erode, opening)
    skel_dst2 = cv2.bitwise_or(skel_dst2, tmp)
    A2 = erode.copy()
    # done = cv2.countNonZero(A2) != 0   #대상이 비어있으면 false
    enable = cv2.countNonZero(A2) > 0  #대상이 비어있으면 false


cv2.imshow('src', src)
cv2.imshow('skel_dst1', skel_dst1)
cv2.imshow('skel_dst2', skel_dst2)

cv2.waitKey()
cv2.destroyAllWindows()

