import cv2
import numpy as np

img = cv2.imread('Fig0310.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x = np.arange(256)
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
table = np.interp(x, xp, fp).astype('uint8')
img1 = cv2.LUT(img, table)
cv2.imshow("Output1", img1)

xp = [0, 90, 128, 192, 255]
fp = [0, 32, 60, 150, 255]
table = np.interp(x, xp, fp).astype('uint8')
img2 = cv2.LUT(img, table)
cv2.imshow("Output2", img2)

xp = [0, 100, 128, 0, 255]
fp = [0, 8, 100, 200, 255]
table = np.interp(x, xp, fp).astype('uint8')
img3 = cv2.LUT(img, table)
cv2.imshow("Output3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows() 