# 0207.py

import cv2
# from matplotlib import pyplot as plt

import time

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('./data/vtest.avi')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
print('frame_size =', frame_size)

while True:
    retval, frame = cap.read()

    if not retval:
        break

    # 정상출력
    cv2.imshow('frame', frame)

    # cv2.imshow(f'frame_{time.time()}', frame)

    # 엣지검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,200)
    cv2.imshow('edges', edges)

    key = cv2.waitKey(25) #0.025, 40fps
    # key = cv2.waitKey(1000) #0.025, 40fps
    if key == 27: #esc
        break
    # time.sleep()
    pass

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()

