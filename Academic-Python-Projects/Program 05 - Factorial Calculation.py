#Program 4 - Factorial for a given input

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive call
    
# Test the function with different values
num = int(input("Enter a number: "))
if num < 0:
    raise ValueError("Factorial is defined only for non-negative integers.")
result = factorial(num)
print(f"Factorial of {num} is {result}")
