#0214.py

import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Video(animation.FuncAnimation):

    def __init__(self, device = 0, fig = None, frames = None, interval = 50, repeat_delay = 5, blit = False, **kwargs):
        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.manager.set_window_title('Video Capture')

            plt.axis('off')

        super(Video, self).__init__(self.fig, self.updateFrame, init_func = self.video_init, frames = frames, interval = interval, blit = blit, repeat_delay = repeat_delay, **kwargs)

        self.cap = cv2.VideoCapture(device)
        print("start capture ...")
        
    def video_init(self):
        print("videoInit")
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        
        
    def updateFrame(self, k):
        print("updateFrame")
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def close(self):
        print("close")
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture.')


camera = Video('./data/vtest.avi')
print("before plt.show")
plt.show()
print("after plt.show")
camera.close()

# 싱글톤, singleton