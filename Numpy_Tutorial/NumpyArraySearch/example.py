import numpy as np

arr=np.array([1,2,3,4,5,4,4])
arr1=np.array([1,2,3,4,5,6,7,8])
arr2=np.array([1,2,3,4,5,6,7,8])

x=np.where(arr==4)
print(x)
print("")
np.where(arr1%2==0)
print(x)
print("")
np.where(arr2%2==1)
print(x)