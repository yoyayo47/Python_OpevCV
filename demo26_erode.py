import cv2
import matplotlib
from matplotlib import pyplot as plt

matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'
FILENAME = './images/image6.jpg'

image = cv2.imread(FILENAME)

ksize = (3, 3)
#ksize = (5, 5)
k1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize)

morphImage = image.copy()
for _ in range(3):
    morphImage = cv2.erode(morphImage, k1)

plt.subplot(121)
plt.imshow(image)
plt.title("normal")
plt.subplot(122)
plt.imshow(morphImage)
plt.title("after erode")
plt.show()
