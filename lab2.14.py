import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Fig0342.tif')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) 

plt.subplot(2,2,1),plt.imshow(img_blur, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(edges, cmap = 'gray')
plt.title('edges'), plt.xticks([]), plt.yticks([])

plt.show()