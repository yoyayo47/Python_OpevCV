import os
import cv2
import matplotlib
from matplotlib import pyplot as plt

print(os.getcwd())
# IMAGE_PATH = ".\\images\\number_zero.jpg"
# IMAGE_PATH = r".\images\number_zero.jpg"
# IMAGE_PATH = "./images/number_zero.jpg"
IMAGE_PATH = "images/number_zero.jpg"
image1 = cv2.imread(IMAGE_PATH, 0)
print("影像是{}, 維度是:{}".format(type(image1), image1.shape))  # row by col
print("每個像素的型態是:{}".format(image1.dtype))
print("取得(0,0)是:{}".format(image1[0, 0]))
print("取得(1,6)是:{}".format(image1[1, 6]))
print("取得(1,7)是:{}".format(image1[1, 7]))
image1[0, 0] = 255
image1[0, 1] = 255
image1[1, 0] = 255
image1[1, 1] = 255
image1[1:6, 1:6] = 128
print(image1)
cv2.imshow("顯示的內容", image1)
plt.imshow(image1)
plt.colorbar()
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'
plt.figure()
plt.imshow(image1)
plt.colorbar()
plt.show()
