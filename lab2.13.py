import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img0 = cv2.imread('Fig0340.tif')

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
gaussianBlur = cv2.GaussianBlur(gray,(5,5),0)

out_arr = np.add(gray, -gaussianBlur)

unSharpened = cv2.addWeighted(gray, 2, out_arr, -0.5, 0)

dst = cv2.addWeighted(gray, 1, unSharpened,1, 0.0)

plt.subplot(2,2,1),plt.imshow(img0, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(gaussianBlur, cmap = 'gray')
plt.title('gaussianBlur'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(unSharpened,cmap = 'gray')
plt.title('unSharpened'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(dst, cmap = 'gray')
plt.title('sharpen'), plt.xticks([]), plt.yticks([])

plt.show()