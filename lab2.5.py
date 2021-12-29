import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('Fig0314.tif',0)
img = np.array(img1)

out = []

for k in range(1, 8):

    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)

    res = cv2.bitwise_and(plane, img)

    x = res * 255
    
    out.append(x)

cv2.imshow("bit plane", np.hstack(out))
cv2.waitKey()