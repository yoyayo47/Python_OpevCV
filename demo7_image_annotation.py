import cv2
from matplotlib import pyplot as plt

FILE_NAME = "./images/google_seminar.jpg"

image = cv2.imread(FILE_NAME, -1)  # 這是預設
# image = cv2.imread(FILE_NAME, 1) #這是彩色
# image = cv2.imread(FILE_NAME, 0) # 這是黑白
print(image.shape)
plt.imshow(image[:, :, ::-1])
plt.title("original image")
# plt.show()

plt.figure()
imageCopy = image.copy()
for i in range(20):
    cv2.line(imageCopy, (200 + 30 * i, 80 - 20 * i), (1200 - 50 * i, 320 + 40 * i), (100 + 5 * i, 100, 255 - 10 * i)
             , thickness=10, lineType=cv2.LINE_AA)
plt.title("image with arbitrary line width, color, AA")
plt.imshow(imageCopy[:, :, ::-1])

plt.figure()
imageCopy = image.copy()
for i in range(20):
    cv2.circle(imageCopy, (250 + 70 * i, 50), 100, (0, 0 + 20 * i, 255 - 20 * i),
               thickness=5 + 2 * i, lineType=cv2.LINE_AA)
cv2.circle(imageCopy, (250, 100), 100, (255, 255, 255), thickness=-1,
           lineType=cv2.LINE_AA)
plt.title("image with circle")
plt.imshow(imageCopy[:, :, ::-1])

plt.figure()
imageCopy = image.copy()
for i in range(20):
    cv2.ellipse(imageCopy, (250, 150), (300, 80), 0 + 40 * i, 0, 360,
                (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
plt.title("image with ellipse")
plt.imshow(imageCopy[:, :, ::-1])

plt.figure()
imageCopy = image.copy()
cv2.ellipse(imageCopy, (250, 150), (250, 80), 0, 180, 360,
            (0, 255, 0), thickness=3, lineType=cv2.LINE_AA)
cv2.ellipse(imageCopy, (300, 250), (250, 80), 0, 180, 360,
            (0, 255, 0), thickness=-1, lineType=cv2.LINE_AA)

plt.imshow(imageCopy[:, :, ::-1])

plt.figure()
imageCopy = image.copy()
text1 = "Hello OPEN CV"
cv2.putText(imageCopy, text1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 100),
            thickness=4, lineType=cv2.LINE_AA)
cv2.putText(imageCopy, text1, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 6, (100, 255, 255),
            thickness=7, lineType=cv2.LINE_AA)

plt.imshow(imageCopy[:, :, ::-1])

plt.show()
