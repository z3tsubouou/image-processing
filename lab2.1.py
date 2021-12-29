import cv2
import numpy as np
import matplotlib.pyplot as plt

import math

img = cv2.imread('skull.tif')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height = img.shape[0]
width = img.shape[1]


print ("zurag uusgeh")
new_img = []

count = 1

for k in range(7):
    tmp_img = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            gray_img[i,j] = math.pow(2,count) * math.floor(gray_img[i, j] / math.pow(2,count))
            tmp_img[i, j] = np.uint8(gray_img[i,j])
    new_img.append(tmp_img)
    count += 1

images = [img] + new_img

fig=plt.figure()
rows = 4
cols = 4
axes=[]

for i in range(len(images)):
    fig.add_subplot(rows, cols, i+1)
    plt.subplot(rows,cols,i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()