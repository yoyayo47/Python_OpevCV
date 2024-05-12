import cv2
import numpy as np
import os
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (16.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = './images/image8.jpg'

image = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)
# plt.imshow(image)
# plt.show()
th, imageBlackWhite = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# plt.imshow(imageBlackWhite)
# plt.show()

x, imLabels = cv2.connectedComponents(imageBlackWhite)
print(type(x), x)
print(type(imLabels), imLabels)
print("max component=", imLabels.max())
nComponents = imLabels.max()
displayRows = int(np.ceil(nComponents / 3.0))
plt.figure()
for i in range(nComponents + 1):
    plt.subplot(displayRows, 3, i + 1)
    plt.imshow(imLabels == i)
    if i == 0:
        plt.title("background id=".format(i))
    else:
        plt.title("component id={}".format(i))
plt.show()

# explain more
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imLabels)
print(minVal, maxVal)
print(type(minLoc), type(maxLoc))
print(minLoc)
print(maxLoc)
imLabels = 255 * (imLabels - minVal) / (maxVal - minVal)
imLabels = np.uint8(imLabels)
imColorMap = cv2.applyColorMap(imLabels, cv2.COLORMAP_RAINBOW)
plt.imshow(imColorMap[:, :, ::-1])
plt.show()
