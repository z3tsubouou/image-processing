import cv2
import numpy as np

img = cv2.imread('Fig0310.tif')
shape = cv2.imread('Fig0432.tif')

img = cv2.resize(img, (1000, 1000), interpolation = cv2.INTER_LINEAR)
shape = cv2.resize(shape, (1000, 1000), interpolation = cv2.INTER_LINEAR)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_shape = cv2.cvtColor(shape,cv2.COLOR_BGR2GRAY)

row, column = gray_img.shape
shapeRow, shapeColumn = gray_shape.shape

img1 = np.zeros((row,column),dtype = 'uint8')
img2 = np.zeros((row,column),dtype = 'uint8')

first = int(row / 11)
second = int(column / 7)

for a, b in zip(range(row), range(shapeRow)):
    for c, d in zip(range(column), range(shapeColumn)):
        if gray_shape[b,d] > 128:
            img1[a,c] = gray_img[a,c]
        else:
            img1[a,c] = 0

for a, b in zip(range(row), range(shapeRow)):
    for c, d in zip(range(column), range(shapeColumn)):
        if gray_shape[b,d] < 128:
            img2[a,c] = gray_img[a,c]
        else:
            img2[a,c] = 0

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.waitKey(0)