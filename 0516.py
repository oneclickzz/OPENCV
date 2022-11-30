#0513.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

#1
# src = cv2.imread('./data/tsukuba_l.png', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('/home/dongkyu/data/cat2.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

#2
dst = cv2.equalizeHist(src)
cv2.imshow('dst', dst)

#3
clahe2 = cv2.createCLAHE(clipLimit = 40, tileGridSize= (1,1))
dst2 = clahe2.apply(src)
cv2.imshow('dst2', dst2)

#4
clahe3 = cv2.createCLAHE(clipLimit = 40, tileGridSize= (8,8))
dst3 = clahe3.apply(src)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()

