#summarizing pandas - DAY 20
print("Day 20 - pandas - Mini Challenge summarizing concepts studied so far")
print("\n")

import pandas as pd

data = {
    'name': ['ajay', 'bala', 'charan', 'dheena', 'elakiya'],
    'subject': ['maths', 'science', 'english', 'science', 'maths'],
    'marks': [88, 92, 75, 95, 33],
    'city': ['chennai', 'cbe', 'cbe', 'madurai', 'chennai'],
    'joined': ['2023-01-10', '2022-12-15', '2023-02-20', '2023-03-01', '2022-11-30']
}

df = pd.DataFrame(data)

def grade(a):
    if a>= 95:
        return 'A'
    elif a>=75:
        return 'B'
    elif a>= 55:
        return 'C'
    else:
        return 'INVALID'
    
df['grade'] = df['marks'].apply(grade)

df['Pass or Fail'] = df['marks'].apply(lambda x:'Pass' if x>=36 else 'Fail')

df['joined'] = pd.to_datetime(df['joined'])

df['year'] = df['joined'].dt.year

df['weekday'] = df['joined'].dt.day_name()

marg = df.groupby(['subject', 'city'])['marks'].mean()
print(marg)
print("\n")

df.to_csv('FINAL TASK FOR PANDAS.csv' , index=False)
df = pd.read_csv('FINAL TASK FOR PANDAS.csv')
print(df.head())
