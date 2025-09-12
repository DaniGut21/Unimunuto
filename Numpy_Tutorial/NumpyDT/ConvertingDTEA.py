import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)
print("")

arr2 = np.array([1.1, 2.1, 3.1])

newarr2 = arr2.astype(int)

print(newarr2)
print(newarr2.dtype)
print("")

arr3 = np.array([1,0,3])

newarr3 = arr3.astype(bool)

print(newarr3)
print(newarr3.dtype)