#Program 9 - Managing Workshop registrations for students from different departments

'''(a) Creates two sets: one for students from Computer Science (CS) and another for
Electronics (ECE) who have registered.
(b) Print the list of students in both sets.
(c) Find and print the students who are common in both departments (i.e., those who
registered from both CS and ECE).
(d) Find and print the students who are unique to each department.
(e) Prints the total number of unique students who have registered (i.e., union of both sets).
(f) Checks if all CS students are also registered in ECE.'''

# (a) Create sets for CS and ECE registered students
cs_students = {"Alice", "Bob", "Charlie", "David"}
ece_students = {"Charlie", "Eve", "Frank", "Bob"}

# (b) Print both sets
print("\nCS Registered Students:", cs_students)
print("ECE Registered Students:", ece_students)

# (c) Common students (intersection)
common_students = cs_students &amp; ece_students
print("\nStudents registered in both CS and ECE:", common_students)

# (d) Unique students in each department (symmetric difference)
unique_students = cs_students ^ ece_students
print("\nStudents unique to each department:", unique_students)

# (e) Total unique students (union)
all_students = cs_students | ece_students
print("\nTotal unique registered students:", all_students)

# (f) Check if CS students are a subset of ECE students and vice versa
print("\nAre all CS students also in ECE?", cs_students.issubset(ece_students))
print("Are all ECE students also in CS?", ece_students.issubset(cs_students))
