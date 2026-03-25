#day 17
print("Day 17 - Pandas - Applying Functions to Columns")
df = pd.DataFrame({
    'name': ['ajay', 'bala', 'charan', 'dheena', 'elakiya'],
    'subject': ['maths', 'science', 'maths', 'english', 'science'],
    'marks': [88, 92, 66, 85, 90]
})
print(df)
print("\n")

def grade(m):
    if m >= 90:
        return 'A'
    elif m >= 75:
        return 'B'
    else:
        return 'C'
df['grade'] = df['marks'].apply(grade)
df['pass/fail'] = df['marks'].apply(lambda x: 'Pass' if x >=40 else 'Fail')
print(df)
print("\n")

#tasks for day 17
df = pd.DataFrame({
    'name': ['ajeesh', 'balan', 'charanika', 'dheenaki', 'elakiya sri'],
    'subject': ['social science', 'science', 'maths', 'english', 'tamil'],
    'marks': [88, 33, 66, 95, 90]
})
print(df)
print("\n")

def grade(m):
    if m >= 90:
        return 'A'
    elif m >= 75 and m <= 89:
        return 'B'
    else:
        return 'C'
    
df['grade'] = df['marks'].apply(grade)
df['pass/fail'] = df['marks'].apply(lambda x: 'Yes' if x >=40 else 'No')

def remark(q):
    if q>=95:
        return 'GOOD'
    elif q>=75:
        return 'BAD'
    else:
        return 'UGLY'
df['remarks'] = df['marks'].apply(remark)
print(df)
