import numpy as np

l1 = [[[40, 40], [289, 40], [289, 289], [40, 289]]]
array1 = np.array(l1)
print(type(array1), array1)
print(array1.shape)
array2 = array1.squeeze()
print(array2.shape)
print(array2)

a3 = np.expand_dims(array2, 0)
print(a3.shape)
print(a3)
a4 = np.expand_dims(a3, 0)
print(a4.shape)
print(a4)
b4 = a4.squeeze()
print(b4.shape)
print(b4)
a5 = np.expand_dims(array2, 1)
print(a5.shape)
print(a5)
a6 = np.expand_dims(array2, 2)
print(a6.shape)
print(a6)