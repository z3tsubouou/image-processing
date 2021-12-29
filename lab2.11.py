import cv2
import numpy
from matplotlib import pyplot as plt

# image path 
path = r'Fig0335.tif'

# using imread()  
img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dst0 = cv2.medianBlur(img,3)
dst1 = cv2.medianBlur(img,7)

fig1=plt.figure("Histogram")
rows = 1
cols = 3
axes=[]

fig1.add_subplot(rows, cols, 1)
plt.subplot(rows,cols, 1)
plt.imshow(img, 'gray')
plt.xticks([])
plt.yticks([])

fig1.add_subplot(rows, cols, 2)
plt.subplot(rows,cols, 2)
plt.imshow(dst0, 'gray')
plt.xticks([])
plt.yticks([])

fig1.add_subplot(rows, cols, 3)
plt.subplot(rows,cols, 3)
plt.imshow(dst1, 'gray')
plt.xticks([])
plt.yticks([])

plt.show()
