# 0411.py
import cv2
import numpy as np

src = cv2.imread('/home/dongkyu/data/lena.jpg')
shape = src.shape[0], src.shape[1], 3
red = np.zeros(shape, dtype = np.uint8)
green = np.zeros(shape, dtype = np.uint8)
blue = np.zeros(shape, dtype = np.uint8)

dst = cv2.split(src)

red[:, :, 2] = dst[2]   # R-채널
green[:, :, 1] = dst[1]   # G-채널
blue[:, :, 0] = dst[0]   # B-채널

cv2.imshow('red', red)
cv2.imshow('green', green)
cv2.imshow('blue', blue)
cv2.waitKey()
cv2.destroyAllWindows()