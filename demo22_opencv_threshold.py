import cv2
from matplotlib import pyplot as plt
import time

IMAGE_PATH = "./images/grayscale-rose1.jpg"
src = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

THRESHOLD_VALUE = 127
MAX_VALUE = 255

t = time.time()
# in ipython you can use
# %timeit cv2.threshold(src, THRESHOLD_VALUE, MAX_VALUE, cv2.THRESH_BINARY)
th, dst = cv2.threshold(src, THRESHOLD_VALUE, MAX_VALUE, cv2.THRESH_BINARY)
print("花了{}秒".format(time.time() - t))
print(f"threshold={th}, type of dst={type(dst)}")

plt.figure(figsize=[15, 8])
plt.subplot(1, 2, 1)
plt.imshow(src, cmap='gray', vmin=0, vmax=255)
plt.subplot(1, 2, 2)
plt.imshow(dst, cmap='gray', vmin=0, vmax=255)
plt.show()
