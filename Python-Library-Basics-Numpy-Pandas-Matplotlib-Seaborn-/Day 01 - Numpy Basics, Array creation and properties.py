#DAY 1 - NUMPY
print("INTRODUCTION TO NUMPY")
print("\n")
print("NumPy (Numerical Python) is a powerful library for numerical computing.")
print("It provides multi-dimensional arrays, mathematical operations, and performance optimization compared to Python lists.")
print("Uses of NumPy - faster computation, uses less memory, built-in functions")
print("\n")
#installed numpy on system using command - pip install numpy
#importing numpy
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print("\n")
'''Creating a simple 1D array
for numbers from 10 to 50'''
dw=np.array([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50])
print(dw)
print("\n")

print("Different ways to create an array")
z = np.zeros((3,3))
print(z)
print("\n")

o = np.ones((2,4))
print(o)
print("\n")

range_arr = np.arange(1,10,2)
print(range_arr)
print("\n")

q = np.linspace(0,10,5)
print(q)
print("\n")

r = np.ones((3,3))
print(r)
print("\n")

p = np.arange(1,21,2)
print(p)
print("\n")

arr = np.array([[1,2,3], [4,5,6]])
print("Shape: ", arr.shape)
print("Size: ", arr.size)
print("Data Type: ", arr.dtype)
print("\n")

jaa = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
print(jaa)
print(jaa.shape)
print(jaa.size)
print(jaa.dtype)
print("\n")
