#0211.py

import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()

def handle_close(event):
    print("close figure!")
    cap.release()


# plt 클래스 설정 (전역 설정)
# plt.ioff()
# plt.show()
plt.axis('off')
plt.ion() #대화 모드


fig = plt.figure(figsize=(10, 6))

# 윈도우타이틀
fig.canvas.manager.set_window_title('Video Capture')

# 이벤트설정
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)


# 플레이설정


# 첫번째 프레임 캡쳐
retval, frame = cap.read()
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# 3
while True:
    retval, frame = cap.read()
    if not retval:
        break

    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()
    # plt.pause(0.001)

    fig.canvas.flush_events() # plt.pause(0.001)

if cap.isOpened():
    cap.release()
