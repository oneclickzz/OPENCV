#0611.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

src = cv2.imread('/home/dongkyu/data/alphabet.bmp', cv2.IMREAD_GRAYSCALE)
tmp_A = cv2.imread('/home/dongkyu/data/A.bmp', cv2.IMREAD_GRAYSCALE)
tmp_S = cv2.imread('/home/dongkyu/data/S.bmp', cv2.IMREAD_GRAYSCALE)
tmp_I = cv2.imread('/home/dongkyu/data/tmp_I.bmp', cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(shape=cv2.MORPH_CROSS, ksize=(3,3))
tmp_S = cv2.erode(tmp_S, kernel, iterations=5)

tmp_b = cv2.imread('/home/dongkyu/data/b.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

#1
R1 = cv2.matchTemplate(src, tmp_A, cv2.TM_SQDIFF_NORMED)
minVal, _, minLoc, _ = cv2.minMaxLoc(R1)
print('TM_SQDIFF_NORMED:', minVal, minLoc)
h, w = tmp_A.shape[:2]
cv2.rectangle(dst, minLoc, (minLoc[0] + w, minLoc[1] + h), (255,0,0), 2)

#2
R2 = cv2.matchTemplate(src, tmp_S, cv2.TM_CCORR_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R2)
print('TM_CCORR_NORMED:', maxVal, maxLoc)
h, w = tmp_S.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (0,255,0), 2)

#3
R3 = cv2.matchTemplate(src, tmp_b, cv2.TM_CCOEFF_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R3)
print('TM_CCORR_NORMED:', maxVal, maxLoc)
h, w = tmp_b.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (0,0,255), 2)

#4
R4 = cv2.matchTemplate(src, tmp_I, cv2.TM_CCOEFF_NORMED)
_, maxVal, _, maxLoc = cv2.minMaxLoc(R4)
print('TM_CCORR_NORMED:', maxVal, maxLoc)
h, w = tmp_I.shape[:2]
cv2.rectangle(dst, maxLoc, (maxLoc[0] + w, maxLoc[1] + h), (255,0,255), 2)

cv2.imshow('dst', dst)
cv2.imshow('tmp_A', tmp_A)
cv2.imshow('tmp_S', tmp_S)
cv2.imshow('tmp_b', tmp_b)
cv2.imshow('tmp_I', tmp_I)

cv2.waitKey()
cv2.destroyAllWindows()