import cv2
from matplotlib import pyplot as plt
import time

IMAGE_PATH = "./images/grayscale-rose1.jpg"
src = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

THRESHOLD_VALUE = 127
MAX_VALUE = 255

th, dst = cv2.threshold(src, THRESHOLD_VALUE, MAX_VALUE, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
th3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 3)
print(type(dst))
print(type(th2))
print(type(th3))
images = [src, dst, th2, th3]
titles = ['origin', 'global thresh=127', 'adaptive mean', 'adaptive gaussian']
index = 0
for (i, t) in zip(images, titles):
    plt.subplot(2, 2, index + 1)
    plt.imshow(i, cmap='gray')
    plt.title(t)
    index += 1
plt.show()