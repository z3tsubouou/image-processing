import cv2
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img0 = cv2.imread('Fig0338.tif')

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian_without_scaling = cv2.Laplacian(img, cv2.CV_64F)

abs_dst = cv2.convertScaleAbs(laplacian_without_scaling)

sharpened = cv2.addWeighted(gray, 1.5, img, -1, 0)

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian_without_scaling,cmap = 'gray')
plt.title('laplacian_without_scaling'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(abs_dst,cmap = 'gray')
plt.title('laplacian_with_scaling'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sharpened, cmap = 'gray')
plt.title('laplacian_with_scaling'), plt.xticks([]), plt.yticks([])

plt.show()