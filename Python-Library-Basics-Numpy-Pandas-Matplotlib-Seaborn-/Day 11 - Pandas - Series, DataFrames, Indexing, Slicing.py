print("Day 11 - Pandas - Series, DataFrames, Indexing, Slicing")
#creating series
import pandas as pd
data = [10,20,30,40]
s = pd.Series(data)
print(s)
print("\n")

#creating a data frame
data = {
    'name': ['ajay','bala','cHaranN'],
    'sCORE': [88,92,95]
    }
df = pd.DataFrame(data)
print(df)
print("\n")

#accessing elements-columns
print(df['name'])
print(df.sCORE)
print(df.columns)
print("\n")

#accessing rows
print(df.loc[0]) #with label 0(label-based indexing)
print(df.iloc[1]) #with index 0(integer based indexing)
print("\n")

#slicing rows
print(df[0:2])
print("\n")

#descriptive statistics
print(df.describe())
print(df.info())
print("\n")

#tasks for day 1
amm = [1,2,3,4,5]
app = pd.Series(amm)
print(app)
print("\n")

giri = {
    'class' : [8,9,10],
        'nickname': ['superman', 'spiderman','batman']
        }
leap = pd.Series(giri)
print(leap)
print("\n")

daf = pd.DataFrame(giri)
print(daf)
print(daf.loc[0])
print(daf.iloc[1])
print(daf['class'])
print(daf['nickname'])
print(daf[0:2])
print(daf.describe())
print(daf.info())
daf['City'] = ['cbe','chn','oot']
print(daf)
print("\n")










