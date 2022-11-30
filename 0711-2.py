#0710.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


# 비디오 캡쳐준비 0번 카메라가 메인카메라, 간혹 1일때가 있음
# 해당 웹캠의 usb는 다른곳에서 사용중이지 않아야함 (usb포트는 하나의 연결만 지원)
cap = cv2.VideoCapture(0)

frameSize = (
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), #넓이
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), #높이
)
print('frame_size =', frameSize)

# shape = (높이,넓이)
mask = np.zeros(shape=(frameSize[1], frameSize[0]), dtype=np.uint8)
markers = np.zeros(shape=(frameSize[1], frameSize[0]), dtype=np.int32)

while True:

    key = cv2.waitKey(30)
    if key == 0x1B:  #esc, 27
        break

    retval, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    bImage = cv2.inRange(hsv, (0,0,120), (255,50,255))  #하얀색
    bImage = cv2.bitwise_not(bImage)

    # bImage = (hsv2 > 0).astype(np.uint8) * 255

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # retval, bImage = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # retval, bImage = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # cv2.imshow('bImage', bImage)

    # 1 1 1 1
    # 1 1 1 1
    # 1 1 1 1
    # 1 1 1 1

    # 거리계산에 대한 식이 포함된 주소
    # L1, L2, C, L12, FAIR, WELSCH, HUBER, USER
    # https://076923.github.io/posts/C-opencv-44/
    dist = cv2.distanceTransform(bImage, cv2.DIST_L2, 3)
    dist8 = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype= cv2.CV_8U)

    # dist_2 = cv2.distanceTransform(bImage, cv2.DIST_L2, 3)
    # dist8_2 = cv2.normalize(dist_2, None, 0, 255, cv2.NORM_MINMAX, dtype= cv2.CV_8U)

    cv2.imshow('dist8', dist8)
    # cv2.imshow('dist8_2', dist8_2)

    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(dist)
    mask = (dist > maxVal * 0.1).astype(np.uint8) * 255
    # cv2.imshow('mask', mask)

    constours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('len(contours)=', len(constours))
    markers[:,:] = 0 #초기화

    markerCount = 0

    for i, cnt in enumerate(constours):
        # cv2.drawContours(markers, [cnt], 0, i+1, -1)

        # cnt 면적으로 필터
        area = cv2.contourArea(cnt)
        # arcLen = cv2.arcLength(cnt, True)

        # print('area=', area)
        # print('arcLen=', arcLen)
        if area <= 6000:
            continue
        
        markerCount += 1
        cv2.drawContours(markers, [cnt], 0, markerCount, -1)

    print('markerCount: ', markerCount)

    cv2.watershed(frame, markers)

    dst = frame.copy()
    dst[markers == -1] = [0,0,255]  #경계선

    # for i in range(len(constours)): #분할영역
    for i in range(markerCount): #분할영역
    
        # r = np.random.randint(256)
        # g = np.random.randint(256)
        # b = np.random.randint(256)
        r = ((i+1) * 32) % 256
        g = ((i+1) * 64) % 256
        b = ((i+1) * 128) % 256
        dst[markers == i+1] = [b,g,r]
        
    dst = cv2.addWeighted(frame, 0.4, dst, 0.6, 0)  #합성

    # # 마커를 시각적으로 표시
    # cv2.circle(dst, (10,10), 10, (255,255,255), 2)
    # cv2.circle(dst, (frameSize[0]//2,frameSize[1]//2), 10, (255,255,255), 2)

    cv2.imshow('dst', dst)

cv2.destroyAllWindows()