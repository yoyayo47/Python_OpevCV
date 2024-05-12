import cv2
from matplotlib import pyplot as plt
import time

IMAGE_PATH = "./images/grayscale-rose1.jpg"
src = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

THRESHOLD_VALUE = 150
MAX_VALUE = 255

THRESHOLDS = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]
images = [src]
descriptions = ["origin", "binary", "binary inverse", "trunc", "thresh to zero", "thresh to zero inverse"]
for t in THRESHOLDS:
    _, dst = cv2.threshold(src, THRESHOLD_VALUE, MAX_VALUE, t)
    images.append(dst)
t = time.time()
print("花了{}秒".format(time.time() - t))

print(len(images))
plt.figure(figsize=[20, 8])
for x in range(1, 7):
    plt.subplot(2, 3, x)
    plt.imshow(images[x - 1], cmap='gray', vmin=0, vmax=255)
    plt.title(descriptions[x - 1])
plt.show()
