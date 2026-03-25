#Program 4

'''Write a program to display the pattern of stars given as follows
*
* *
* * *
* * * *
* * * * *'''

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Loop to print the pattern
for i in range(1, rows + 1):
    print("*" * i) 
