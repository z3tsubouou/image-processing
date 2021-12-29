import cv2
import numpy as np

img = cv2.imread('Fig0312.tif')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
row, column = gray_img.shape

img1 = np.zeros((row,column),dtype = 'uint8')
img2 = np.zeros((row,column),dtype = 'uint8')

min_range = 140
max_range = 240

for i in range(row):
    for j in range(column):
        if gray_img[i,j] > min_range and gray_img[i,j] < max_range:
            img1[i,j] = 200
        else:
            img1[i,j] = 0

min_range = 140
max_range = 240
min_range1 = 35
max_range2 = 75

for i in range(row):
    for j in range(column):
        if gray_img[i,j] > min_range and gray_img[i,j] < max_range:
            img2[i,j] = 180
        elif gray_img[i,j] > min_range1 and gray_img[i,j] < max_range2:
            img2[i,j] = gray_img[i,j]
        else:
            img2[i,j] = 0

#  Display the image
cv2.imshow('sliced image', img1)
cv2.imshow('sliced image2', img2)
cv2.waitKey(0)