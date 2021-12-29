import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Fig0333.tif')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
row, column = gray_img.shape

dst3 = cv2.GaussianBlur(gray_img, (3,3), cv2.BORDER_DEFAULT)
dst5 = cv2.GaussianBlur(gray_img, (5,5), cv2.BORDER_DEFAULT)
dst9 = cv2.GaussianBlur(gray_img, (9,9), cv2.BORDER_DEFAULT)
dst15 = cv2.GaussianBlur(gray_img, (15,15), cv2.BORDER_DEFAULT)
dst35 = cv2.GaussianBlur(gray_img, (35,35), cv2.BORDER_DEFAULT)
 
img1 = np.zeros((row,column),dtype = 'uint8')
img2 = np.zeros((row,column),dtype = 'uint8')
img3 = np.zeros((row,column),dtype = 'uint8')
img4 = np.zeros((row,column),dtype = 'uint8')
img5 = np.zeros((row,column),dtype = 'uint8')

img1 = dst3
img2 = dst5
img3 = dst9
img4 = dst15
img5 = dst35

images = [img, img1, img2, img3, img4, img5]

fig=plt.figure()
rows = 3
cols = 2
axes=[]

for i in range(len(images)):
    fig.add_subplot(rows, cols, i+1)
    plt.subplot(rows,cols,i+1)
    plt.imshow(images[i], 'gray')
    plt.xticks([])
    plt.yticks([])

plt.show()