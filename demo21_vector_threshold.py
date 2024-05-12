import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

IMAGE_PATH = "./images/grayscale-rose1.jpg"
src = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

THRESHOLD_VALUE = 150
MAX_VALUE = 255


def thresholdUsingVector(sourceImage, threshold, maxValue):
    dst = np.zeros_like(sourceImage)
    maxPixels = src > threshold
    minPixels = src <= threshold
    dst[maxPixels] = maxValue
    dst[minPixels] = 0
    return dst


t = time.time()
dst = thresholdUsingVector(src, THRESHOLD_VALUE, MAX_VALUE)
print("花了{}秒".format(time.time() - t))

# fact1 0.001 <-- copy image

plt.figure(figsize=[15, 8])
plt.subplot(1, 2, 1)
plt.imshow(src, cmap='gray', vmin=0, vmax=255)
plt.subplot(1, 2, 2)
plt.imshow(dst, cmap='gray', vmin=0, vmax=255)
plt.show()
