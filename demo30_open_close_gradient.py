import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = './images/mickey.jpg'

image = cv2.imread(FILENAME)

# ksize = (3, 3)
# ksize = (5, 5)
ksize = (7, 7)
k1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)

morphImage = image.copy()
METHODS = [cv2.MORPH_GRADIENT, cv2.MORPH_OPEN, cv2.MORPH_CLOSE]
images = [image]
descriptions = ['original', 'gradient', 'open', 'close']
for m in METHODS:
    returnImage = cv2.morphologyEx(morphImage, m, k1)
    images.append(returnImage)

plt.figure(figsize=[10, 6])
index = 1
for i, d in zip(images, descriptions):
    plt.subplot(1, 4, index)
    plt.imshow(i)
    plt.title(d)
    index += 1
plt.show()
