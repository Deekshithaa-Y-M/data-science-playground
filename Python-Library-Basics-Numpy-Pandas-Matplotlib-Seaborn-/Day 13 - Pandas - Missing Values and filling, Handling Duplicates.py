print("Day 13 - Pandas - Missing Values, Filling Null Values, Handling Duplicates, Replacing Values")
import pandas as pd
import numpy as np

data = {
    'name': ['ajay', 'bala', np.nan, 'charan', 'bala', 'ajay', 'deepak', 'elakiya'],
    'marks': [88, 0, 75, np.nan, 0, 88, 92, np.nan],
    'subject': ['maths', 'science', 'english', 'maths', 'science', 'maths', 'english', 'science']
}

df = pd.DataFrame(data)

print("🎯 Original Data:")
print(df)
print(df.isnull().sum())
df.fillna(0)
print(df)
df['marks'] = df['marks'].fillna(df['marks'].mean())
print(df)
print("\n")

#dropping rows when names is missing ^_~
df.dropna(subset=['name'], inplace=True)
print(df)
print("\n")

#removing duplicates
df = df.drop_duplicates()
print(df)
print("\n")

#replacing duplicates
df['marks'] = df['marks'].replace(0,'absent')
print(df)
print("\n")

#day 13 tasks
#creating a dataframe
sun = {
    'names' : ['ser' , 'jai' , 'jof' , 'myrce', 'tywin' , 'tyrill', np.nan],
    'rating' : [97,99,0,np.nan,95,99,0],
    'children':['deck' , 'bath' , np.nan, np.nan, 'wish' , np.nan,0]
    }

df =  pd.DataFrame(sun)
df.drop_duplicates()
print(df)
print("\n")

df['rating'] = df['rating'].fillna(df['rating'].mean())
df['children'] = df['children'].fillna('no children')
df.dropna(subset=['names'], inplace = True)
df['rating'] = df['rating'].replace(0,'absent')
print(df)
print("\n")


    


