#Program 1 - Calculating Average and Total Marks for three subjects

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Loop through each student
for i in range(num_students):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter student name: ") # Get student details
    mark1 = int(input("Enter marks in Subject 1: "))
    mark2 = int(input("Enter marks in Subject 2: "))
    mark3 = int(input("Enter marks in Subject 3: "))
    total = mark1 + mark2 + mark3 # Calculate total and average
    average = total / 3
    print("\nStudent Name:", name) # Display student details - individually
    print("Total Marks:", total)
    print("Average Marks:", average)
