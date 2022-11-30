# 0418.py
import cv2
import numpy as np

src1 = cv2.imread('/home/dongkyu/data/lena.jpg')
src2 = cv2.imread('/home/dongkyu/lena111.jpg')
src3 = cv2.imread('/home/dongkyu/lena222.jpg')

#3
black_and = cv2.bitwise_and(src1, src2)
cv2.imshow('black_and', black_and)
white_and = cv2.bitwise_and(src1, src3)
cv2.imshow('white_and', white_and)

#4
black_or = cv2.bitwise_or(src1, src2)
cv2.imshow('black_or', black_or)
white_or = cv2.bitwise_or(src1, src3)
cv2.imshow('white_or', white_or)

cv2.waitKey(0)
cv2.destroyAllWindows()