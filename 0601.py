#0601.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

src = cv2.imread('/home/dongkyu/data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.boxFilter(src, ddepth=-1, ksize=(11,11))
dst2 = cv2.boxFilter(src, ddepth=-1, ksize=(31,31))
dst3 = cv2.bilateralFilter(src, d=21, sigmaColor=10, sigmaSpace=10)
dst4 = cv2.bilateralFilter(src, d=-1, sigmaColor=10, sigmaSpace=10)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

cv2.waitKey()
cv2.destroyAllWindows()

