import cv2
from matplotlib import pyplot as plt
import matplotlib

FILE_NAME = "images/ms.jpg"
matplotlib.rcParams['image.cmap'] = 'gray'

image = cv2.imread(FILE_NAME)
print("彩色影象的維度{}".format(image.shape))
x1 = cv2.split(image)
print(type(x1), len(x1), type(x1[0]), x1[0].shape)
b, g, r = cv2.split(image)
plt.figure(figsize=[20, 5])
plt.subplot(1, 4, 1)
plt.imshow(b)
plt.title("blue channel")
plt.subplot(1, 4, 2)
plt.imshow(g)
plt.title("green channel")
plt.subplot(1, 4, 3)
plt.imshow(r)
plt.title("red channel")
plt.subplot(144)
imageMerged = cv2.merge((r, g, b))
plt.imshow(imageMerged)
plt.title("construct back")
plt.show()
