#Program 11

'''Write a Python program using NumPy to:
(a) Create a 1D NumPy array with 10 random integers between 1 and 100.
(b) Print the array.
(c) Find and print the maximum and minimum values in the array.
(d) Calculate and print the sum and mean of the array elements.
(e) Extract and print all even numbers from the array.
(f) Create a 3x3 matrix with random integers between 1 and 50 and print it.
(g) Find and print the sum of all elements in the matrix.
(h) Compute and print the transpose of the matrix.'''

import numpy as np
# (a) Create a 1D NumPy array with 10 random integers between 1 and 100
arr = np.random.randint(1, 101, 10)

# (b) Print the array
print("Array:", arr)

# (c) Find max and min values
print("Maximum Value:", np.max(arr))
print("Minimum Value:", np.min(arr))

# (d) Calculate sum and mean
print("Sum of elements:", np.sum(arr))
print("Mean of elements:", np.mean(arr))

# (e) Extract and print all even numbers
even_numbers = arr[arr % 2 == 0]
print("Even Numbers:", even_numbers)

# (f) Create a 3x3 matrix with random integers between 1 and 50
matrix = np.random.randint(1, 51, (3, 3))
print("\nMatrix:\n", matrix)

# (g) Find the sum of all elements in the matrix
print("Sum of matrix elements:", np.sum(matrix))

# (h) Compute and print the transpose of the matrix
print("Transpose of the matrix:\n", matrix.T)
