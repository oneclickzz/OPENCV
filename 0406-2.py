# 0406.py
import cv2
import numpy as np

x1, y1 = 240, 250
x2, y2 = 360, 280

src = cv2.imread('/home/dongkyu/data/lena.jpg')
shape = y2-y1, x2-x1, 3
dst = np.zeros(shape, dtype = src.dtype)

# src = cv2.imread('/home/dongkyu/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# dst = np.zeros(shape = (y2-y1, x2-x1), dtype = src.dtype)

N = 10
h = (y2 - y1) // N + 1
w = (x2 - x1) // N + 1

for i in range(h):
    for j in range(w):
        y = i * N
        x = j * N
        # dst[y:y+N, x:x+N] = cv2.mean(src[y1+y:y1+y+N, x1+x:x1+x+N])[0] # 그레이스케일 영상
        dst[y:y+N, x:x+N] = cv2.mean(src[y1+y:y1+y+N, x1+x:x1+x+N])[0:3] # 컬러 영상

src[y1:y2, x1:x2] = dst
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()