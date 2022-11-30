# 0406.py
import cv2
import numpy as np

src = cv2.imread('/home/dongkyu/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)

img = src[roi[1]:roi[1] + roi[3],
          roi[0]:roi[0] + roi[2]]

N = 8
h = roi[3] // N + 1
w = roi[2] // N + 1

for i in range(h):
    for j in range(w):
        y = i * N
        x = j * N
        img[y:y+N, x:x+N] = cv2.mean(img[y:y+N, x:x+N])[0] # 그레이스케일 영상
        # dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3] # 컬러 영상

src[roi[1]:roi[1] + roi[3],
    roi[0]:roi[0] + roi[2]] = img

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()