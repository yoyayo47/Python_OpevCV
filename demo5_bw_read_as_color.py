import cv2
from matplotlib import pyplot as plt
import matplotlib

FILE_NAME = "images/number_zero.jpg"
matplotlib.rcParams['image.cmap'] = 'gray'
image = cv2.imread(FILE_NAME, 1)
print(type(image), image.shape)
plt.imshow(image)
plt.title("black/white as color")
plt.show()
print("[0,0] -->", image[0, 0])
print("[3,3] -->", image[3, 3])
print("[6,6] -->", image[6, 6])

plt.figure(figsize=[14, 6])
image[0, 0] = (0, 0, 255)
plt.subplot(1, 3, 1)
plt.imshow(image[:, :, ::-1])
image[1, 1] = (0, 255, 0)
plt.subplot(1, 3, 2)
plt.imshow(image[:, :, ::-1])
image[2, 2] = (255, 0, 0)
plt.subplot(1, 3, 3)
plt.imshow(image[:, :, ::-1])
plt.show()
