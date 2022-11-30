# 0505.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('/home/dongkyu/data/lena.jpg')
histColor =('b','g','r')
for i in range(3):
    hist1 = cv2.calcHist(images = [src], channels= [i], mask = None,
                    histSize=[256], ranges=[0,256])
    plt.plot(hist1, color = histColor[i])
plt.show()