import numpy as np
import cv2
import math

img = cv2.imread("coins.jpeg")

count = 0

coins500 = [
    [131,131,111,49.7],
    [134,131,110,49.6],
    [126,132,119,49.9],
    [125,136,123,49.4],
    [123,133,123,50.4],
    [126,134,120,48.3],
]

coins50 = [
    [129,131,113,41],
    [123,134,119,38.7],
]

coins100 = [
    [122,134,122,43.8],
    [124,132,123,45.7],
    [126,132,119,44.6],
    [131,132,110,42.2],
    [129,134,116,44.9],
    [128,135,119,44.1],
    [132,133,111,43.6],
    [137,129,105,43.8],
    [137,130,110,43.8],
    [140,129,109,43.6],
    [143,131,116,44.0],
]

coins10 = [
    [102,141,136,43.2],
    [103,140,137,42.5],
    [103,141,137,43],
    [103,141,143,42.2],
    [103,142,134,43],
    [107,139,136,43],
    [107,142,141,41.8],
    [113,136,134,41.6],
]

coins500 = np.array(coins500)
coins100 = np.array(coins100)
coins50 = np.array(coins50)
coins10 = np.array(coins10)

labels = [500,100,50,10]

radius_mean = [
    np.mean(coins500[:,3]),
    np.mean(coins100[:,3]),
    np.mean(coins50[:,3]),
    np.mean(coins10[:,3]),
]

radius_diff = [
    np.max(coins500[:,3]) - np.min(coins500[:,3]),
    np.max(coins100[:,3]) - np.min(coins100[:,3]),
    np.max(coins50[:,3]) - np.min(coins50[:,3]),
    np.max(coins10[:,3]) - np.min(coins10[:,3]),
]

silver = np.concatenate((coins500, coins100, coins50), axis = 0)
gold = np.array(coins10)
gold_mean = np.mean(gold[:,0:3], axis = 0)
silver_mean = np.mean(silver[:,0:3], axis = 0)

def calculateColorDist(a, b):
    d0 = a[0] - b[0]
    d1 = a[1] - b[1]
    d2 = a[2] - b[2]
    dist = math.sqrt(d0*d0 + d1*d1 + d2*d2)
    return dist

def calculateRadius(radius):
    suggested = []
    for i, mean in enumerate(radius_mean):
        if radius >= mean - radius_diff[i] and radius <= mean + radius_diff[i]:
            suggested.append(abs(mean - radius))
    suggested.sort()
    return suggested

def detect(avg_color, radius):
    gold_dist = calculateColorDist(gold_mean, avg_color)
    silver_dist = calculateColorDist(silver_mean, avg_color)
    min_color = min(gold_dist, silver_dist)
    all_radiuses = calculateRadius(radius)
    if len(all_radiuses) == 0:
        return 0

    for min_radius in all_radiuses:
        if min_color == silver_dist:
            if min_radius == abs(radius_mean[0]-radius):
                return 500
            elif min_radius == abs(radius_mean[1]-radius):
                return 100
            elif min_radius == abs(radius_mean[2]-radius):
                return 50
        if min_color == gold_dist:
            if min_radius == abs(radius_mean[3]-radius):
                return 10
    return 0

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 50, param1=100, param2=30, minRadius= 25, maxRadius=55)

for x, y, radius in circles[0,:]:
    img_crop = img[(int)(y-radius):(int)(y+radius),(int)(x-radius):(int)(x+radius)]

    img_crop = cv2.GaussianBlur(img_crop, (7,7), 0)
    img_ycc = cv2.cvtColor(img_crop, cv2.COLOR_BGR2YCR_CB)
    img_ycc[:,:,0] = cv2.equalizeHist(img_ycc[:,:,0])
    img_crop = cv2.cvtColor(img_ycc, cv2.COLOR_YCrCb2RGB)

    avg_color = np.average(img_crop, axis=0)
    avg_color = np.average(avg_color, axis=0)

    value = detect(avg_color, radius)
    count += value

    cv2.circle(img, (int(x),int(y)), 1, (255, 0, 0), 2)
    cv2.circle(img, (int(x),int(y)), int(radius), (255, 0, 0), 2)

    cv2.putText(img, str(value), (int(x), int(y)), 0, 0.5, 255)

cv2.imshow("detected circles", img)
cv2.waitKey(0)