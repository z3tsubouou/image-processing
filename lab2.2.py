import cv2
import matplotlib.pyplot as plt

img = cv2.imread("rose1024.tif")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

resized128 = cv2.resize(gray_img, (128,128), interpolation=cv2.INTER_LINEAR)
resized64 = cv2.resize(gray_img, (64,64), interpolation=cv2.INTER_LINEAR)
resized32 = cv2.resize(gray_img, (32,32), interpolation=cv2.INTER_LINEAR)

cv2.imwrite("/Users/macintosh/Documents/hicheel/hewtanilt/lab2/rose128.png", resized128)
cv2.imwrite("/Users/macintosh/Documents/hicheel/hewtanilt/lab2/rose64.png", resized64)
cv2.imwrite("/Users/macintosh/Documents/hicheel/hewtanilt/lab2/rose32.png", resized32)

resized1024v2 = cv2.resize(resized32, (1024,1024),fx = 10, fy = 10, interpolation=cv2.INTER_LINEAR)
resized1024v3 = cv2.resize(resized64, (1024,1024),fx = 10, fy = 10, interpolation=cv2.INTER_LINEAR)
resized1024v4 = cv2.resize(resized128, (1024,1024),fx = 10, fy = 10, interpolation=cv2.INTER_LINEAR)

cv2.imwrite("/Users/macintosh/Documents/hicheel/hewtanilt/lab2/rose1024v2.png", resized1024v2)
cv2.imwrite("/Users/macintosh/Documents/hicheel/hewtanilt/lab2/rose1024v3.png", resized1024v3)
cv2.imwrite("/Users/macintosh/Documents/hicheel/hewtanilt/lab2/rose1024v4.png", resized1024v4)
