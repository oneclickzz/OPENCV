# 0209.py

import cv2
# from matplotlib import pyplot as plt

# pip install pafy
# pip install youtube_dl

# ..lib\site-packages\pafy\backend_youtube_dl.py", line 53
# like_count, dislike_count

import pafy
# url = 'http://www.youtube.com/watch?v=u_Q7Dkl7AIk'
url = 'https://www.youtube.com/watch?v=Yb4saNDmddU'

video = pafy.new(url)
best = video.getbest()

# https://rr3---sn-ab02a0nfpgxapox-bh2zr.googlevideo.com/videoplayback?expire=1667549211&ei=u3NkY82FCo7c4wLx0qKICA&ip=115.95.212.93&id=o-AKK_6511gECY4x3kEadK_P1Nv5zkv7WDL00fb826U9p3&itag=22&source=youtube&requiressl=yes&mh=RW&mm=31%2C26&mn=sn-ab02a0nfpgxapox-bh2zr%2Csn-n4v7snl7&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=772500&vprv=1&mime=video%2Fmp4&ns=PeU-GxZ8etoP40HcdDDPh3EI&cnr=14&ratebypass=yes&dur=29.094&lmt=1665658107584408&mt=1667527304&fvip=5&fexp=24001373%2C24007246&c=WEB&txp=5318224&n=9iFlDiZZIVO9tY4Jsd&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAINkdaLK_xhktkF2rSVpOU2r866k7lq4ksp09zl7CDKpAiEAwgNgEfXToaT3AoTsXCNG_6bTBc5E0RE0kZ1EdEnU74Y%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAMQNIF4O2jyfPphBUfv-TYsp99qZgKefPoRXxkp4iJodAiBfue3OIGU4psahZTSK5z0Ln0WTzrqFj17doVO1gqxMyQ%3D%3D

# print(f'title: {video.title}')
# print(f'best url: {best.url}')

# cap = cv2.VideoCapture(best.url)
cap = cv2.VideoCapture('https://rr3---sn-ab02a0nfpgxapox-bh2zr.googlevideo.com/videoplayback?expire=1667549211&ei=u3NkY82FCo7c4wLx0qKICA&ip=115.95.212.93&id=o-AKK_6511gECY4x3kEadK_P1Nv5zkv7WDL00fb826U9p3&itag=22&source=youtube&requiressl=yes&mh=RW&mm=31%2C26&mn=sn-ab02a0nfpgxapox-bh2zr%2Csn-n4v7snl7&ms=au%2Conr&mv=m&mvi=3&pl=16&initcwndbps=772500&vprv=1&mime=video%2Fmp4&ns=PeU-GxZ8etoP40HcdDDPh3EI&cnr=14&ratebypass=yes&dur=29.094&lmt=1665658107584408&mt=1667527304&fvip=5&fexp=24001373%2C24007246&c=WEB&txp=5318224&n=9iFlDiZZIVO9tY4Jsd&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAINkdaLK_xhktkF2rSVpOU2r866k7lq4ksp09zl7CDKpAiEAwgNgEfXToaT3AoTsXCNG_6bTBc5E0RE0kZ1EdEnU74Y%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAMQNIF4O2jyfPphBUfv-TYsp99qZgKefPoRXxkp4iJodAiBfue3OIGU4psahZTSK5z0Ln0WTzrqFj17doVO1gqxMyQ%3D%3D')
# cap = cv2.VideoCapture(url)
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

    cv2.imshow('frame', frame)

    key = cv2.waitKey(25) #0.025, 40fps
    if key == 27: #esc
        break
    # time.sleep()
    pass

if cap.isOpened():
    cap.release()

cv2.destroyAllWindows()

