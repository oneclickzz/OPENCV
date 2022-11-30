#0201.py

import cv2
import numpy as np

imageFile = '/home/dongkyu/data/lena.jpg'
img = cv2.imread(imageFile)

# cv2.IMREAD_UNCHANGED == -1, cv2.IMREAD_GRAYSCALE == 0, cv2.IMREAD_COLOR == 1
img2 = cv2.imread(imageFile, 0)

# img3 = cv2.imread(imageFile, cv2.IMREAD_UNCHANGED)
# img4 = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
# img5 = cv2.imread(imageFile, cv2.IMREAD_COLOR)

# img6 = cv2.imread('./data/transparent.png', cv2.IMREAD_COLOR)

# encode_img = np.fromfile(imageFile, np.uint8)
# img = cv2.imdecode(encode_img, cv2.IMREAD_GRAYSCALE)

# if flag == 0:
#     # 그레이
# elif flag == 1:
#     # 컬러

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

# cv2.imshow('IMREAD_UNCHANGED', img3)
# cv2.imshow('IMREAD_GRAYSCALE', img4)
# cv2.imshow('IMREAD_COLOR', img5)

# cv2.imshow('transparent', img6)



cv2.waitKey()
cv2.destroyAllWindows()