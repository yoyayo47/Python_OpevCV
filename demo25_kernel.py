import cv2
from matplotlib import pyplot as plt

kernel = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]

plt.figure(figsize=[15, 8])
SIZE = 3
i = 1
for k in kernel:
    a1 = cv2.getStructuringElement(k, (SIZE, SIZE))
    plt.subplot(1, 3, i)
    plt.imshow(a1, 'gray')
    i += 1
plt.show()
