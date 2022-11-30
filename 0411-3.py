# 0411.py
import cv2
import numpy as np


def merge(list):

    if not list or len(list) <= 0:
        return np.zeros((0,0), np.uint8)

    mat = list[0]
    count = len(list)
    dst = np.zeros((mat.shape[0], mat.shape[1], count), mat.dtype)

    for i in range(count):
        mat = list[i]
        # print('mat shape: ', mat.shape)
        # (512,512,1)

        if len(mat.shape) > 2:
            if mat.shape[2] > 1:
                raise TypeError
            dst[:,:,i] = mat[:,:,0]
            continue
        # dst[:,:,i] = mat[:,:]
        dst[:,:,i] = mat

    return dst

src = cv2.imread('/home/dongkyu/data/lena.jpg') #bgr
zeros = np.zeros((src.shape[0], src.shape[1], 1), np.uint8)
# zeros = np.zeros((src.shape[0], src.shape[1], 3), np.uint8)

b,g,r = cv2.split(src)
# bMat = cv2.merge([b,zeros,zeros])
# gMat = cv2.merge([zeros,g,zeros])
# rMat = cv2.merge([zeros,zeros,r])
bMat = merge([b,zeros,zeros])
gMat = merge([zeros,g,zeros])
rMat = merge([zeros,zeros,r])

cv2.imshow('blue', bMat)
cv2.imshow('green', gMat)
cv2.imshow('red', rMat)

cv2.waitKey()
cv2.destroyAllWindows()