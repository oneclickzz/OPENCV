# 0603-2.py
import cv2
import numpy as np
import time
import matplotlib as plt

src = cv2.imread('/home/dongkyu/data/rect.jpg', cv2.IMREAD_GRAYSCALE)

gx = cv2.Sobel(src, -1, 1, 0, ksize = 3, delta = 128)
gy = cv2.Sobel(src, -1, 0, 1, ksize = 3, delta = 128)

cv2.imshow('src', src)
cv2.imshow('gx', gx)
cv2.imshow('gy', gy)

cv2.waitKey()
cv2.destroyAllWindows()