import cv2
from matplotlib import pyplot as plt
import matplotlib

FILE_NAME = "images/opencv.png"
image = cv2.imread(FILE_NAME, -1)
print("alpha channel, color image type=", type(image))
print("影像讀成矩陣的維度是:", image.shape)
plt.title("direct read")
plt.imshow(image)
plt.show()

correctedImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.title("color correction")
plt.imshow(correctedImage)
plt.show()
print("轉換後的顏色是:",correctedImage.shape)

imageBGR = image[:,:,:3]
imageAlphaMask = image[:,:,3]
plt.figure(figsize=[12,8])
plt.subplot(121)
plt.title("Color channel")
plt.imshow(imageBGR[:,:,::-1])
plt.subplot(122)
plt.imshow(imageAlphaMask)
plt.title("Alpha channel")
plt.show()