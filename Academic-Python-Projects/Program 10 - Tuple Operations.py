#Program 10

'''You are given a tuple containing random numbers. Write a Python program that:
(a) Creates a tuple with at least 10 different numbers.
(b) Prints all elements of the tuple.
(c) Accesses and prints the first and last elements of the tuple.
(d) Finds and prints the maximum and minimum values in the tuple.
(e) Counts how many times a specific number appears in the tuple.
(f) Finds the index of a specific number in the tuple.
(g) Creates a new tuple by slicing the first 5 elements.
(h) Reverses the tuple and prints it.'''

# (a) Create a tuple with random numbers
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# (b) Print the tuple
print("Tuple elements:", numbers)

# (c) Access and print the first and last elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# (d) Find the maximum and minimum values in the tuple
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# (e) Count how many times a number appears in the tuple
num_to_count = int(input("Enter a number to count: "))
print(f"{num_to_count} appears {numbers.count(num_to_count)} times in the tuple.")

# (f) Find the index of a specific number in the tuple
num_to_find = int(input("Enter a number to find its index: "))
if num_to_find in numbers:
    print(f"{num_to_find} is at index {numbers.index(num_to_find)}")
else:
    print(f"{num_to_find} is not in the tuple.")

# (g) Create a new tuple by slicing (Extract first 5 elements)
sliced_tuple = numbers[:5]
print("First 5 elements:", sliced_tuple)

# (h) Reverse the tuple
reversed_tuple = numbers[::-1]
print("Reversed tuple:", reversed_tuple)
