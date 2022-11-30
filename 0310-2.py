#0310.py
import cv2
import numpy as np


KEY_MAP = {
    100: 0,
    115: 1,
    97: 2,
    119: 3,
}

OFFSETS = (
    (10, 0), 
    (0, 10), 
    (-10, 0), 
    (0, -10)
)

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0  #right

while True:
    key = cv2.waitKeyEx(30)
    # key = cv2.waitKey(30)
    # print('key: ', key)

    if key == 0x1B: # 27(10)
        break

    # 입력된 키의 방향으로 이동 (입력이 없을시엔 가장 최근 움직인 방향을 유지)
    direction = KEY_MAP.get(key, direction)
    x += OFFSETS[direction][0]
    y += OFFSETS[direction][1]

    # 반전
    # 오 -> 왼 0 -> 2, 왼 -> 오 2 -> 0, 아 -> 위 1 -> 3, 위 -> 아 3 -> 1 


    #경계확인 (특정 경계에 닿으면 반대 방향으로 반전)
    if x < R:
        x = R
        direction = 0 #right 로 반전
    
    if x > width - R:
        x = width - R
        direction = 2 #left 로 반전
    
    if y < R:
        y = R
        direction = 1 #down 으로 반전
    
    if y > height - R:
        y = height - R
        direction = 3 #up 으로 반전

    #지우고 그리기
    img = np.zeros((width,height,3), dtype=np.uint8) + 255 #지우기
    cv2.circle(img, (x,y), R, (0,0,255), -1)
    cv2.imshow('img', img)


cv2.destroyAllWindows()