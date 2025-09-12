import numpy as np

arr=np.array([41,42,43,44])
arr1=np.array([1,2,3,4,5,6,7])
filter_arr=[]
filter_arr1=[]
for element in arr:
    if element>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
for element in arr1:
    if element % 2==0:
        filter_arr1.append(True)
    else:
        filter_arr1.append(False)

newarr=arr[filter_arr]
newarr1=arr1[filter_arr1]

print(filter_arr)
print(newarr)
print("")
print(filter_arr1)
print(newarr1)