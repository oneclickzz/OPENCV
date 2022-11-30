#0509.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


# 1. cv2.HISTCMP_CORREL : 상관관계
# 1: 완전 일치, -1: 완전 불일치, 0: 무관계
# 빠르지만 부정확

# 2. cv2.HISTCMP_CHISQR : 카이제곱 검정(Chi-Squared Test)
# 0: 완전 일치, 무한대: 완전 불일치

# 3. cv2.HISTCMP_INTERSECT : 교차
# 1: 완전 일치, 0: 완전 불일치(히스토그램이 1로 정규화된 경우)

# 4. cv2.HISTCMP_BHATTACHARYYA : 바타차야 거리
# 0: 완전 일치, 1: 완전 불일치
# 느리지만 가장 정확

# 5. EMD
# 직관적이지만 가장 느림


#1
nPoints = 100000
pts1 = np.zeros((nPoints, 1), dtype = np.uint16)
pts2 = np.zeros((nPoints, 1), dtype = np.uint16)

cv2.setRNGSeed(int(time.time()))
cv2.randn(pts1, mean=(128), stddev= (10))
cv2.randn(pts2, mean=(110), stddev= (20))

#2
H1 = cv2.calcHist(images=[pts1], channels=[0], mask=None, histSize=[256], ranges=[0,256])
cv2.normalize(H1, H1, 1, 0, cv2.NORM_L1)

plt.plot(H1, color = 'r', label = 'H1')

H2 = cv2.calcHist(images=[pts2], channels=[0], mask = None, histSize=[256], ranges=[0,256])
cv2.normalize(H2, H2, 1, 0, cv2.NORM_L1)

#3
d1 = cv2.compareHist(H1, H2, cv2.HISTCMP_CORREL)
d2 = cv2.compareHist(H1, H2, cv2.HISTCMP_CHISQR)
d3 = cv2.compareHist(H1, H2, cv2.HISTCMP_INTERSECT)
d4 = cv2.compareHist(H1, H2, cv2.HISTCMP_BHATTACHARYYA)

print('d1(H1, H2, CORREL)=', d1)  #클수록 유사, 상관관계
print('d2(H1, H2, CHISQR)=', d2)  #작을수록 유사, 카이제곱
print('d3(H1, H2, INTERSECT)=', d3) #클, 교차
print('d4(H1, H2, BHATTACHARYYA)=', d4) #작, 바타차야 거리



plt.plot(H2, color = 'b', label = 'H2')

plt.legend(loc = 'best')
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()