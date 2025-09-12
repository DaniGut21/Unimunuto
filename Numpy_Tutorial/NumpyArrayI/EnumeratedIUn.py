import numpy as np

arr=np.array([1,2,3])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
print("")

arr2=np.array([[1,2,3,4], [5,6,7,8]])

for idx, x in np.ndenumerate(arr2):
    print(idx, x)