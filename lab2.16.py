import numpy as np
import cv2
from matplotlib import pyplot as plt

# Reading the Image
img = cv2.imread("yawts.png", cv2.IMREAD_UNCHANGED)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

domainFilter = cv2.edgePreservingFilter(img, flags=1, sigma_s=60, sigma_r=0.6)

gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
gaussBlur2 = cv2.GaussianBlur(img,(9,9),cv2.BORDER_DEFAULT)

kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(img,-1,kernel)

medianFilter = cv2.medianBlur(img,5)

# Bilateral filter
print("Bilateral Filter")
bilFil = cv2.bilateralFilter(img, 60, 60, 60)

highPass = img - gaussBlur
highPass2 = img - gaussBlur2

lowPass = cv2.filter2D(img, -1, kernel)
lowPass2 = cv2.filter2D(img, 3, kernel)

lowPass = img - lowPass
lowPass2 = img - lowPass2

plt.subplot(2,5,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,2),plt.imshow(domainFilter,cmap = 'gray')
plt.title('domainFilter'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,3),plt.imshow(gaussBlur,cmap = 'gray')
plt.title('gaussBlur'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,4),plt.imshow(meanFilter,cmap = 'gray')
plt.title('meanFilter'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,5),plt.imshow(medianFilter,cmap = 'gray')
plt.title('medianFilter'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,6),plt.imshow(bilFil,cmap = 'gray')
plt.title('bilFil'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,7),plt.imshow(highPass,cmap = 'gray')
plt.title('highPass'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,8),plt.imshow(lowPass,cmap = 'gray')
plt.title('lowPass'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,9),plt.imshow(highPass2,cmap = 'gray')
plt.title('highPass'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,10),plt.imshow(lowPass2,cmap = 'gray')
plt.title('lowPass'), plt.xticks([]), plt.yticks([])

plt.show()