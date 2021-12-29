import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Fig0310.tif')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

x = np.arange(256)
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
table = np.interp(x, xp, fp).astype('uint8')
img1 = cv2.LUT(img, table)

xp = [0, 90, 128, 192, 255]
fp = [0, 32, 60, 150, 255]
table = np.interp(x, xp, fp).astype('uint8')
img2 = cv2.LUT(img, table)

xp = [0, 100, 128, 0, 255]
fp = [0, 8, 100, 200, 255]
table = np.interp(x, xp, fp).astype('uint8')
img3 = cv2.LUT(img, table)

Verti = np.concatenate((img, img1, img2, img3), axis=0)

cv2.imshow('Images', Verti)

equal = cv2.equalizeHist(img)
equal1 = cv2.equalizeHist(img1)
equal2 = cv2.equalizeHist(img2)
equal3 = cv2.equalizeHist(img3)

equalEval = np.concatenate((equal, equal1, equal2, equal3), axis=0)
cv2.imshow('equalize', equalEval)

fig=plt.figure("Histogram")
rows = 4
cols = 1
axes=[]

histr = cv2.calcHist([img],[0],None,[256],[0,256])
histr1 = cv2.calcHist([img1],[0],None,[256],[0,256])
histr2 = cv2.calcHist([img2],[0],None,[256],[0,256])
histr3 = cv2.calcHist([img3],[0],None,[256],[0,256])

fig.add_subplot(rows, cols, 1)
plt.subplot(rows,cols, 1)
plt.plot(histr)

fig.add_subplot(rows, cols, 2)
plt.subplot(rows,cols, 2)
plt.plot(histr1)

fig.add_subplot(rows, cols, 3)
plt.subplot(rows,cols, 3)
plt.plot(histr2)

fig.add_subplot(rows, cols, 4)
plt.subplot(rows,cols, 4)
plt.plot(histr3)

fig1=plt.figure("Histogram")
rows = 4
cols = 1
axes=[]

equalhistr = cv2.calcHist([equal],[0],None,[256],[0,256])
equalhistr1 = cv2.calcHist([equal1],[0],None,[256],[0,256])
equalhistr2 = cv2.calcHist([equal2],[0],None,[256],[0,256])
equalhistr3 = cv2.calcHist([equal3],[0],None,[256],[0,256])

fig1.add_subplot(rows, cols, 1)
plt.subplot(rows,cols, 1)
plt.plot(equalhistr)

fig1.add_subplot(rows, cols, 2)
plt.subplot(rows,cols, 2)
plt.plot(equalhistr1)

fig1.add_subplot(rows, cols, 3)
plt.subplot(rows,cols, 3)
plt.plot(equalhistr2)

fig1.add_subplot(rows, cols, 4)
plt.subplot(rows,cols, 4)
plt.plot(equalhistr3)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

