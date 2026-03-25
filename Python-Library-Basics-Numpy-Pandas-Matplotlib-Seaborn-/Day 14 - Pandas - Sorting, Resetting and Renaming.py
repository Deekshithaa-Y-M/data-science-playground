#Day 14
print("Day 14 - Pandas - Sorting, Resetting & Renaming in Pandas")
df = pd.DataFrame({
    'name': ['ajay' , 'bala' , 'charan'],
    'marks':[88,95,72]
    })
sorted_df = df.sort_values(by = 'marks' , ascending = False)
print(sorted_df)
reset_df = sorted_df.reset_index(drop = True)
print(reset_df)
print("\n")

#renaming colums
renamed_df = reset_df.rename(columns={'marks':'total'})
print(renamed_df)
print("\n")

#renaming index
renamed_df.index = ['student1' , 'student2' , 'student3']
print(renamed_df)
print("\n")

#tasks for day 14 
df = pd.DataFrame({
    'name' : ['rani' , 'vikas' , 'dakshin' , 'aruvi' , 'anoushka'],
    'marks':[25,75,99,100,33],
    'subject': ['science', 'physics','chemistry' ,'maths','cs']
    })
tar = df.sort_values(by = 'marks')
print(tar)
print("\n")

tar = tar.reset_index(drop = True)
print(tar)
print("\n")

tar = tar.rename(columns={'marks':'total_marks'})
print(tar)
print("\n")

tar.index=['a','b','c','d','e']
print(tar)
