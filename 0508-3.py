# 0508-3.py
import cv2
import numpy as np


src = cv2.imread('/home/dongkyu/infrared_road.jpg')
yuv = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)
y,u,v = cv2.split(yuv)

w = 496 // 7
h = 290 // 5

for i in range(1,5):
    cv2.line(src, (0, h*i), (496, h*i), (255,255,255), 2)
for j in range(1,7):
    cv2.line(src, (w*j, 0), (w*j, 290), (255,255,255), 2)

y_1 = cv2.inRange(y, 80, 255)
c = cv2.bitwise_and(y,y_1)
for i in range(6):
    for j in range(8):
        t = i * h
        x = j * w
        c[t:t+h, x:x+w] = cv2.mean(c[t:t+h, x:x+w])[0] 

font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(0,5):
    for j in range(0,7):
        cv2.putText(src, f'{(c[i*h][j*w])}',((j*w)+3,(i*h)+20), font ,0.6,(0,255,0), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()