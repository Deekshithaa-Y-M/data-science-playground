print("Day 3 - Numpy - Operations and Broadcasting")
import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])

print(a+b)
print(a*b)
print(a ** 2) #supports +, - , * , / , ** , % directly on arrays
print("\n")

#exercise 1
nova = np.array([10,2,3,4,5])
novice = np.array([4,5,6,7,8])
print(nova+novice)
print(nova-novice)
print(nova*novice)
print(nova/novice)
print(novice**2)
print("\n")

arr = np.array([1,4,9,16])

#universal functions
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))
print(np.sin(arr))
print("\n")

#exercise 2
quil = np.array([1,2,3,4,5,6,7,8,9,10])
print(np.sqrt(quil))
print(np.log(quil))
print(np.exp(quil))
print("\n")

#broadcastinG
#Broadcasting lets you perform operations on arrays of different shapes without loops.
arr = np.array([10,20,30])
print(arr + 5)
print("\n")

A = np.array([[1,2,3],
             [4,5,6]])
B = np.array([10,20,30])
print(A+B)
print("\n")

C = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
D = np.array([1,2,3])
print(C+D)
print("\n")
