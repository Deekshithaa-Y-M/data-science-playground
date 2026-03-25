print("Final Day - Numpy - Broadcasting, Logical Comparisons and Recap Challenges")
import numpy as np

#broadcasting
arr2 = np.array([[1,2,3],
                 [4,5,6]])
arr1 = np.array([10,20,30])

res = arr2+arr1
print(res)
print("\n")

arr_1d_vertical = arr1.reshape(3, 1)
print(arr_1d_vertical )
print("\n")

#boolean indexing
nin = np.array([1,33,44,55,66,77,88,99])
caty = nin[nin>50]
print(caty)
print("\n")

#logical conditions
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[(arr>20) & (arr<50)])
print("\n")

edd = np.random.randint(10,99,(6,6))
print(edd)
print("\n")

edd[edd>60] = 999
print(edd)
print("\n")

print(np.std(np.random.rand(99,999,9)))
