import cv2

import os, glob

from os import makedirs

from os.path import join

path = '/Users/macintosh/Documents/hicheel/hewtanilt/images'
dstpath = '/Users/macintosh/Documents/hicheel/hewtanilt/result'
averageDstpath = '/Users/macintosh/Documents/hicheel/hewtanilt/result2/average.jpeg'
dstpath3 = '/Users/macintosh/Documents/hicheel/hewtanilt/result3'

try:
    makedirs(dstpath)
except:
    print ("Huudas ali hediin uussen baina.")

print ("ehlel ........")

image_data = []
os.chdir(path)

for image in glob.glob("*.jpeg"):
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        resizedGray = cv2.resize(gray, (500, 400), interpolation=cv2.INTER_LINEAR)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath, resizedGray)
        image_data.append(resizedGray)

    except Exception as error:
        print ("{} hurwuulj chadsangui".format(error))

print ("hoyordahi ........")

avg_image = image_data[0]

for i in range(len(image_data)):
    if i == 0:
        pass
    else:
        alpha = 1.0/(i + 1)
        beta = 1.0 - alpha
        avg_image = cv2.addWeighted(image_data[i], alpha, avg_image, beta, 0.0)

cv2.imwrite(averageDstpath, avg_image)

print ("barag duuslaa ........")

i = 0
os.chdir(dstpath)

for image in glob.glob("*.jpeg"):
    try:
        img = cv2.imread(os.path.join(dstpath,image))
        subImage = avg_image - image_data[i]
        dstpath3 = join(dstpath3,image)
        cv2.imwrite(dstpath3, subImage)
        i += 1
        dstpath3 = '/Users/macintosh/Documents/hicheel/hewtanilt/result3'

    except Exception as error:
        print ("{} hurwuulj chadsangui".format(error))

print ("duussan .....")