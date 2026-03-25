#Program 2 to read a four-digit number and calculate the sum of its digits.

# Take a four-digit number as input
num = int(input("Enter a four-digit number: "))

# Initialize sum
digit_sum = 0

# Loop to extract and sum digits
while num > 0:
    last_digit = num % 10 # Get the last digit
    digit_sum = digit_sum + last_digit # Add it to the sum
    num = num // 10 # Remove the last digit
    
# Print the result
print("\nSum of digits:", digit_sum)
