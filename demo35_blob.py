import cv2
import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (16.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = './images/image12.jpg'

image = cv2.imread(FILENAME, cv2.IMREAD_COLOR)
th, imageBlackWhite = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
plt.imshow(imageBlackWhite)
plt.show()
# plt.imshow(image)

params = cv2.SimpleBlobDetector.Params()

params.minThreshold = 3
params.maxThreshold = 300

params.filterByArea = True
params.minArea = 1000

params.filterByCircularity = True
#params.minCircularity = 0.5
#params.minCircularity = 0.8

params.filterByInertia = True
#params.minInertiaRatio = 0.01
params.minInertiaRatio = 0.5

detector = cv2.SimpleBlobDetector.create(params)
keypoints = detector.detect(imageBlackWhite)
print(len(keypoints))

for k in keypoints:
    x, y = k.pt
    x = int(round(x))
    y = int(round(y))
    cv2.circle(image, (x, y), 5, (255, 0, 255), -1)
    diameter = k.size
    radius = int(round(diameter / 2))
    cv2.circle(image, (x, y), radius, (0, 0, 255), 2)
plt.imshow(image[:, :, ::-1])
plt.show()
