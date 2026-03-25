print("Day 7 - Numpy - Stacking and Splitting!")
import numpy as np

#stacking and spllitting - to combine arrays and split them into smaller parts
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

'''stacking vertically(row-wise)
checking alphabet positions'''

v_stacked = np.vstack((arr1,arr2))
print("vertically stacked", v_stacked)
print("\n")

#stacking horizontally
h_stacked = np.hstack((arr1,arr2))
print("horizontally stacked: \n", h_stacked)
print("\n")

#exercise 1
arr3 = np.random.randint(1,50,(3,3))
arr4 = np.random.randint(1,50,(3,3))
print(arr3)
print(arr4)
print("\n")

#now stacking them horizontally
har = np.hstack((arr3, arr4))
print(har)
print("\n")

#now stacking them vertically
mar = np.vstack((arr3, arr4))
print(mar)
print("\n")

#concept 2 - splitting and dividing arrays
arr = np.array([[1,2,3,4],[5,6,7,8]])
h = np.hsplit(arr,2)
print(h)
print("\n")

v = np.vsplit(arr,2)
print(v)
print("\n")

#exercise 2
sir = np.random.randint(1,17,(4,4))
print(sir)
print("\n")

y, z = np.vsplit(sir, 2)  # Unpacking both parts
print(y)
print("\n")

print(z)
print("\n")

a, b, c, d = np.vsplit(sir, 4)  # Splitting into 4
print(a)
print("\n")

print(b)
print("\n")

print(c)
print("\n")

print(d)





