import  numpy as np

arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr, 3)
print(newarr)
print("")
newarr2=np.array_split(arr, 4)
print(newarr2)