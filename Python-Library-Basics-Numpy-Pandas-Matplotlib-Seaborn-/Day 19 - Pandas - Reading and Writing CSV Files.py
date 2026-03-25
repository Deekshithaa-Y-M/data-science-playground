#day 19
import pandas as pd

print("Day 19 - Pandas - Reading and Writing CSV Files")
print("\n")

df = pd.DataFrame({
    'name': ['ajay', 'bala', 'charan'],
    'date_joined': ['2023-01-10', '2022-12-15', '2023-02-20']
})

print(df)
print("\n")

df.to_csv('students.csv', index=False)
df = pd.read_csv('students.csv')
print(df.head())
print("\n")

#tasks for day 19
df = pd.DataFrame({
    'name' : ['geronimo' , 'stilton' , 'thea' , 'grace' , 'lucy'],
    'marks' : [98 , 99 , 96 , 94 , 95],
    'subject' : ['eng' , 'math' , 'sci' , 'soc' , 'tamil']
    })

df.to_csv('student2.csv' , index = False)

df = pd.read_csv('student2.csv')
print(df.head(3))
print("\n")
