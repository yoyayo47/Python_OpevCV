import cv2
import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
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
plt.imshow(image[:, :, ::-1])

plt.figure()
for index, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image2, (x, y), (x + w, y + h), (255, 128, 255), 2)
plt.imshow(image2[:, :, ::-1])
plt.show()
