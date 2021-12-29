import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Fig0334.tif')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row, column = gray_img.shape

dst3 = cv2.GaussianBlur(gray_img, (35,35), cv2.BORDER_DEFAULT)

img1 = np.zeros((row,column),dtype = 'uint8')
img2 = np.zeros((row,column),dtype = 'uint8')

img1 = dst3

for a in range(row):
    for c in range(column):
        if gray_img[a,c] > 128:
            img2[a,c] = 255
        else:
            img2[a,c] = 0

images = [img, img1, img2]

fig=plt.figure()
rows = 1
cols = 3
axes=[]

for i in range(len(images)):
    fig.add_subplot(rows, cols, i+1)
    plt.subplot(rows,cols,i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()