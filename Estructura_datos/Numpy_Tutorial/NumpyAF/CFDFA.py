import numpy as np

arr=np.array([41,42,43,44])
arr1=np.array([1,2,3,4,5,6,7])

filter_arr=arr>42
filter_arr1=arr1%2==0

newarr=arr[filter_arr]
newarr1=arr1[filter_arr1]

print(filter_arr)
print(newarr)
print("")
print(filter_arr1)
print(newarr1)