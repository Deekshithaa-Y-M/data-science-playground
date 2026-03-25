print("Day 6 - Numpy - Reshaping and Broadcasting")
import numpy as np

arr = np.arange(1,10)
reshaped_arr = arr.reshape(3,3)

print(reshaped_arr)
print("\n")

#exercise 1
four = np.arange(1,17)
five = four.reshape(4,4)

print(five)
print("\n")

#flattening arrays - convering multi-dimenional arrays into one dimensional arrays
mat = np.array([[1,2,3],[4,5,6]])
flat = mat.flatten()
print(flat)
print("\n")

#execise 2
#using ravel this time for a change
man = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
meh = man.ravel()
print(meh)
print("\n")

#concept 3 - broadcasting
arr = np.array([[1,2,3],[4,5,6]])
vec = np.array([10,20,30])

print(arr+vec)
print("\n")

#exercise 3
rook = np.array([[1,2,3.3],[4.4,5,6],[7,8,9]])
rame = np.array([10,20,30])
print(rook+rame)


