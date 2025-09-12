import numpy as np

arr=np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
arr1=np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
arr2=np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
arr3=np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])

newarr=np.array_split(arr, 3)
print(newarr)
print("")
newarr1=np.array_split(arr1, 3)
print(newarr1)
print("")
newarr2=np.array_split(arr2,3, axis=1)
print(newarr2)
print("")
newarr3=np.hsplit(arr3, 3)
print(newarr3)