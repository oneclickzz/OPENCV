#0510.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

#1
nPoints = 100000
pts1 = np.zeros((nPoints, 1), dtype = np.uint16)
pts2 = np.zeros((nPoints, 1), dtype = np.uint16)

cv2.setRNGSeed(int(time.time()))
cv2.randn(pts1, mean=(128), stddev= (10))
cv2.randn(pts2, mean=(110), stddev= (20))

#2
H1 = cv2.calcHist(images=[pts1], channels=[0], mask=None, histSize=[256], ranges=[0,256])
# cv2.normalize(H1, H1, 1, 0, cv2.NORM_L1)

H2 = cv2.calcHist(images=[pts2], channels=[0], mask = None, histSize=[256], ranges=[0,256])
# cv2.normalize(H2, H2, 1, 0, cv2.NORM_L1)

#3
S1 = np.zeros((H1.shape[0],2), np.float32)
S2 = np.zeros((H1.shape[0],2), np.float32)

for i in range(S1.shape[0]):
    S1[i, 0] = H1[i, 0]
    S2[i, 0] = H2[i, 0]
    S1[i, 1] = i
    S2[i, 1] = i

emd1, lowerBound, flow = cv2.EMD(S1, S2, cv2.DIST_L1)
print('EMD(S1, S2, DIST_L1) =', emd1)

emd2, lowerBound, flow = cv2.EMD(S1, S2, cv2.DIST_L2)
print('EMD(S1, S2, DIST_L2) =', emd2)

emd3, lowerBound, flow = cv2.EMD(S1, S2, cv2.DIST_C)
print('EMD(S1, S2, DIST_C) =', emd3)

plt.plot(H1, color = 'r', label = 'H1')
plt.plot(H2, color = 'b', label = 'H2')
plt.legend(loc = 'best')
plt.show()



cv2.waitKey()
cv2.destroyAllWindows()