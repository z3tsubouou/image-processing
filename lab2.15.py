import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Fig0343.tif')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#a
img = cv2.GaussianBlur(img_gray,(3,3),0)

#b
laplacian_without_scaling = cv2.Laplacian(img, cv2.CV_64F)

#c
Sharpen = cv2.addWeighted(img, 1, img_gray,1, 0.0)

#d
sobel_64 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
abs_64 = np.absolute(sobel_64)
sobel_8u = np.uint8(abs_64)

#e
kernel = np.ones((5,5),np.float32)/25
avg5x5 = cv2.filter2D(img,-1,kernel)

#f
out_arr = np.add(Sharpen, -avg5x5)
    
#g
Sharpen2 = cv2.addWeighted(img, 1, out_arr,1, 0.0)

#h
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)
  
# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)

plt.subplot(2,4,1),plt.imshow(img_gray, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,2),plt.imshow(laplacian_without_scaling,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,3),plt.imshow(Sharpen,cmap = 'gray')
plt.title('Sharpen'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,4),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('sobel_8u'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,5),plt.imshow(avg5x5,cmap = 'gray')
plt.title('avg5x5'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,6),plt.imshow(out_arr,cmap = 'gray')
plt.title('out_arr'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,7),plt.imshow(Sharpen2,cmap = 'gray')
plt.title('Sharpen2'), plt.xticks([]), plt.yticks([])

plt.subplot(2,4,8),plt.imshow(log_transformed,cmap = 'gray')
plt.title('log_transformed'), plt.xticks([]), plt.yticks([])

plt.show()