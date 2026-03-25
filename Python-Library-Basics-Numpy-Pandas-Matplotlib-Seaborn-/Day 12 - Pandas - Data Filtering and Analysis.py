print("Day 12 - Pandas - Data Filtering and Analysis")
data = {
    'Name': ['Ajay', 'Bala', 'Charan', 'Dheena'],
    'Score': [88, 92, 95, 85]
}
df = pd.DataFrame(data)
print(df[df['Score'] > 90])
print("\n")

#multiple conditions and or
print(df[(df['Score'] > 85) & (df['Score'] < 95)])
print(df[(df['Score'] < 88) & (df['Score'] > 94)])
print("\n")

#isin() and between()
print(df[df['Name'].isin(['Ajay' , 'Dheena'])])
print(df[df['Score'].between(85,95)])
print("\n")

#sorting data
print(df.sort_values(by='Score'))
print(df.sort_values(by = 'Name' , ascending=False))
print("\n")

#Day 12 tasks.
dot = {
    'name' : ['Abi' , 'Agan' , 'Brindha' , 'Chinmayi' , 'Deva' , 'Eric'],
    'marks' : [90,98,96,80,85,97],
    'subject': ['science' , 'social' , 'tamil' , 'english' , 'maths' , 'python']
}
df = pd.DataFrame(dot)
print(df)

print(df[df['subject'].isin(['maths' , 'science'])])
print(df[df['marks'] > 90])
print(df[(df['marks']>70) & (df['marks']<90)])
print(df.sort_values(by = 'marks', ascending=False))
print("\n")

def assign_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    else:
        return 'C'

df['grade'] = df['marks'].apply(assign_grade)
print(df)
