#Day 16
print("Day 16 - Pivot Tables and Crosstabs(Excel - style Pandas)")
print("\n")

df = pd.DataFrame({
    'name': ['ajay', 'bala', 'charan', 'dheena', 'elakiya'],
    'subject': ['maths', 'science', 'maths', 'english', 'science'],
    'marks': [88, 92, 75, 85, 90],
    'city': ['chennai', 'cbe', 'cbe', 'madurai', 'cbe']
})
pivot = df.pivot_table(values = 'marks' , index = 'subject' , columns = 'city' , aggfunc = 'mean')
print(pivot)
print("\n")

op = pd.crosstab(df['city'],df['subject'])
print(op)
print("\n")

#tasks for day 16
df = pd.DataFrame({
    'name': ['lyanna', 'jora', 'lyanna', 'dheena', 'elakiya'],
    'subject': ['maths', 'science', 'maths', 'english', 'science'],
    'marks': [88, 92, 73, 85, 90],
    'city': ['chennai', 'cbe', 'trichy', 'madurai', 'cbe']
})
print(df)
print("\n")

mary = df.pivot_table(values='marks' , index = 'subject', columns='city',aggfunc='mean')
print(mary)
print("\n")

loras = pd.crosstab(df['city'],df['subject'])
print(loras)
print("\n")
