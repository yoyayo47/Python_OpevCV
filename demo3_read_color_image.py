import cv2
from matplotlib import pyplot as plt
import matplotlib

FILE_NAME = "images/ms.jpg"
matplotlib.rcParams['image.cmap'] = 'gray'

image = cv2.imread(FILE_NAME)
print("彩色影象的維度{}".format(image.shape))
plt.title("direct read from cv2.imread")
plt.imshow(image)
plt.figure()
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.title("apply cvtColor from BGR back to RGB")
plt.imshow(imageRGB)

plt.figure()
imageReverse = image[:,:,::-1]
plt.title("reverse BGR channel to RGB")
plt.imshow(imageReverse)

plt.show()
