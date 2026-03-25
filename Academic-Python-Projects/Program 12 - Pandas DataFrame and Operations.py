#Program 12

'''Write a Python program using Pandas to:
(a) Create a DataFrame with 5 students' names, their marks in Math and Science.
(b) Print the DataFrame.
(c) Display the student with the highest Math marks.
(d) Calculate and print the average marks in Science.
(e) Add a new column for the total marks (Math + Science).
(f) Sort the DataFrame based on total marks in descending order.'''

import pandas as pd
# (a) Create a DataFrame with student names and marks
data = {
'Name': ['Arun', 'Bala', 'Charan', 'Deepa', 'Elan'],
'Math': [78, 85, 90, 66, 72],
'Science': [88, 79, 95, 73, 80]
}
df = pd.DataFrame(data)

# (b) Print the DataFrame
print("Student Marks DataFrame:\n", df)

# (c) Display the student with the highest Math marks
top_math_student = df.loc[df['Math'].idxmax()]
print("\nStudent with highest Math marks:\n", top_math_student)

# (d) Calculate and print the average marks in Science
avg_science = df['Science'].mean()
print("\nAverage Science Marks:", avg_science)

# (e) Add a new column for total marks
df['Total Marks'] = df['Math'] + df['Science']
print("\nDataFrame with Total Marks:\n", df)

# (f) Sort the DataFrame based on total marks in descending order
df_sorted = df.sort_values(by='Total Marks', ascending=False)
print("\nSorted DataFrame (by Total Marks):\n", df_sorted)
