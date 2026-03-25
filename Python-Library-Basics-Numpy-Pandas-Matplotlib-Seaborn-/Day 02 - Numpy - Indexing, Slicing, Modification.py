print("Day 2 - Numpy - Indexing and Slicing")
import numpy as np
print("\n")
print("INDEXING")
arr = np.array([10,20,30,40,50])
print(arr[0])   # First element → 10
print(arr[2])    # Third element → 30
#negative indexing
print(arr[-1])   # Last element → 50

pi = np.arange(1,21)
print(pi)

print("\n")
print("SLICING")
pi = np.array
print(arr[0]) #index 0
print(arr[-1]) #index from last
print(arr[1:4]) #index 1 to 3
print(arr[:3]) #first 3 elements
print(arr[::2]) #every second element
print(arr[::-1]) #reversed
print(arr[1:21:3]) #start:end:step

#exercise 1
jam = np.arange(1, 21)  # Creates array from 1 to 20

print(jam[:5])   # First 5 elements
print(jam[-4:])  # Last 4 elements
print(jam[::3])  # Every third element
print(jam[::-1]) # Reverse the array


arr2D = np.array([[10,20,30],
                  [40,50,60],
                  [70,80,90]])

print(arr2D[0,1])  # Row 0, Column 1 → 20
print(arr2D[1,:])  # Entire 2nd row → [40, 50, 60]
print(arr2D[:,2])  # Entire 3rd column → [30, 60, 90]

#exercise 2
mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(mat[1,0])
print(mat[1,:])
print(mat[:,2])

#modifying elements
arr = np.array([10,20,30,40])
arr[2] = 99
print(arr)

arr2D[1,1] = 999
print(arr2D)

chu = np.array([1,2,3,4,5,6,7,8,9,10])
chu[chu % 2 == 0] = -1  # Change all even numbers to -1
print(chu)


thr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(thr)
thr[1,1] = 0
print(thr)




