print("Day 8 - Linear algebra in numpy")
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#MATRIX MULTIPLICATION
result = np.dot(A,B)
print(result)
print(A @ B)
print("\n")

#transpose
print(A.T)
print("\n")

#Determinant, inverse , eigen values and eigen vectors
from numpy.linalg import det, inv, eig

print(det(A))
print("\n")

print(inv(A))
print("\n")

print(eig(A))
print("\n")

#tasks for day 8
C = np.random.randint(1,100,(3,3))
D = np.random.randint(1,100,(3,3))
print(C)
print(D)
print("\n")

E = np.dot(C,D)
print(E)
print("\n")

print(D.T)
print("\n")

print(det(C))
print("\n")

print(inv(D))
print("\n")

print(eig(C))
print("\n")

print(C@D)
print("\n")

