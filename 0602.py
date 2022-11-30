#0602.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

src = cv2.imread('/home/dongkyu/data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst1 = cv2.medianBlur(src, ksize=7)
dst2 = cv2.blur(src, ksize=(7,7))
# sigma 2차원 가우시안 커널 표준편차
# sigmaX가 0이 아닐때 sigmaY = sigmaX
# sigmaX = 0, sigmaY = 0 이면 ksize(kw, kh)로 계산
# sigmaX = (0.3*(kw-1)/2-1) + 0.8
# sigmaY = (0.3*(kh-1)/2-1) + 0.8
dst3 = cv2.GaussianBlur(src, ksize=(7,7), sigmaX=0.0)
dst4 = cv2.GaussianBlur(src, ksize=(7,7), sigmaX=10.0)


cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

cv2.waitKey()
cv2.destroyAllWindows()

