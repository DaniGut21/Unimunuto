import numpy as np

arr=np.array([6,7,8,9])
arr1=np.array([6,7,8,9])
arr2=np.array([1,3,5,7])

x=np.searchsorted(arr, 7)
print(x)
print("")
x=np.searchsorted(arr1, 7, side='right')
print(x)
print("")
x=np.searchsorted(arr2, [2,4,6])
print(x)