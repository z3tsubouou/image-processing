import cv2
import numpy as np

img = cv2.imread('Fig0326.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

fi = img / 255.0

gamma = 0.4
gamma2 = 0.01

out = np.power(fi, gamma)
out2 = np.power(fi, gamma2)

cv2.imshow("img", img)
cv2.imshow("out", out)
cv2.imshow("out2", out2)
cv2.waitKey()  