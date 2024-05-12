import cv2
import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (16.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = './images/image11.png'

image = cv2.imread(FILENAME)
# plt.imshow(image)
# plt.show()
image2 = image.copy()
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th, imageBlackWhite = cv2.threshold(imageGray, 20, 255, cv2.THRESH_BINARY)
# plt.imshow(imageBlackWhite)
# plt.show()

contours, hierarchy = cv2.findContours(imageBlackWhite, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(type(contours), len(contours))
print(hierarchy)

cv2.drawContours(image, contours, -1, (0, 255, 255), 3)
# plt.imshow(image[:, :, ::-1])

for index, contour in enumerate(contours):
    M = cv2.moments(contour)
    x = int(round(M["m10"] / M["m00"]))
    y = int(round(M["m01"] / M["m00"]))
    cv2.circle(image, (x, y), 3, (255, 0, 255), -1)
    cv2.putText(image, f"{index + 1}", (x + 40, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
plt.imshow(image[:, :, ::-1])
plt.show()
