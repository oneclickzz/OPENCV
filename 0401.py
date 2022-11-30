# 0401.py
import cv2
import numpy as np

# cv2.IMREAD_UNCHANGED = -1
# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_COLOR = 3
# img = cv2.imread('/home/dongkyu/data/lena.jpg')  # cv2.IMREAD_COLOR
img = cv2.imread('/home/dongkyu/data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print('ima.ndim = ', img.ndim)
print('ima.shape = ', img.shape)
print('ima.dtype = ', img.dtype)

##np.bool, np.uint16, np.uint32,
## np.float32, np.float64, np.complex64
img = img.astype(np.int32)
print('img.dtype = ', img.dtype)

img = np.uint8(img)
print('img.dtype = ', img.dtype)