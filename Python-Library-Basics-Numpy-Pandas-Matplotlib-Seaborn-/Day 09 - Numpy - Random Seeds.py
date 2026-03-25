print("Day 9 - Numpy - Random seeds")

import numpy as np

#Random floats between 0 and 1
print(np.random.rand(3))  #1D Array
print("\n")

print(np.random.rand(2,3))  #2D Array
print("\n")

print(np.random.randint(1,10, size=(3,3)))  #Random integers
print("\n")

#setting a seed - to make results reproducible (important for debugging and testing)
np.random.seed(42)
print(np.random.rand(2,2))
print("\n")

#same seed gives the same results
#checking if it's true
np.random.seed(42)
print(np.random.rand(2,2))
print("\n")

#shuffle and permutation
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)
print("\n")

print(np.random.permutation(arr))
print("\n")

print(np.random.randint(1,100,(4,4)))
print("\n")

np.random.seed(58)
print(np.random.rand(3,3))
print("\n")

np.random.seed(58)
print(np.random.rand(3,3))
print("\n")

one = np.array([1,2,3,4,5,6,7,8,9,99])
print(one)
print("\n")

np.random.shuffle(one)
print(one)
print("\n")

print(np.random.permutation(one))
print("\n")

sansa = np.random.rand(5,5)
#printing rounded decimal using round
r = np.round(sansa, 2)
print(r)
print("\n")

#random - choice - forgot this concept
arr = np.array([1,2,3,4,5])
rd = np.random.choice(arr)
print("Random element:" , rd)
print("\n")

# Generate 5x5 floats between 10 and 50
#low + (high - low) * np.random.rand(shape)

arr = 10 + (50 - 10) * np.random.rand(5, 5)

# Round to 2 decimal places
rounded = np.round(arr, 2)
print(rounded)
print("\n")







