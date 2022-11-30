#0311.py
import cv2
import numpy as np

def onMouse(event, x, y, flags, param):

    print('flags: ', flags)
    # print('param: ', param)

    # if event == cv2.EVENT_LBUTTONDOWN: #마우스 왼쪽 클릭
    if event == cv2.EVENT_LBUTTONUP: #마우스 왼쪽 클릭
        if flags & cv2.EVENT_FLAG_SHIFTKEY: # 시프트 키와 함께
            cv2.rectangle(param[0], (x-5, y-5), (x+5, y+5), (255,0,0))
        else:
            cv2.circle(param[0], (x,y), 5, (255,0,0), 3)

    elif event == cv2.EVENT_RBUTTONDOWN: # 마우스 오른쪽 클릭
        cv2.circle(param[0], (x,y), 5, (0,0,255), 3)

    elif event == cv2.EVENT_LBUTTONDBLCLK: # 마우스 왼쪽 버튼 더블클릭
        param[0] = np.zeros(param[0].shape, np.uint8) + 255

    cv2.imshow('img', param[0])
    pass




img = np.zeros((512,512,3), dtype=np.uint8) + 255
cv2.imshow('img', img)

# 마우스이벤트
cv2.setMouseCallback('img', onMouse, [img])

# cv2.waitKey()

while True:
    key = cv2.waitKey()
    if key == 27:
        break

cv2.destroyAllWindows()