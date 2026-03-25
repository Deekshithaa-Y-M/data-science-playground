print("Day 15 - Pandas - Grouping and Aggregation")
import pandas as pd
#concept 1
df = pd.DataFrame({
    'name': ['ajay', 'bala', 'charan', 'dheena', 'elakiya'],
    'subject': ['maths', 'science', 'maths', 'english', 'science'],
    'marks': [88, 92, 75, 85, 90]
})

grouped = df.groupby('subject')
print(grouped['marks'].mean())
print("\n")

#agg
agg_stats = df.groupby('subject')['marks'].agg(['mean' , 'max' , 'min'])
print(agg_stats)
print("\n")

#tasks for day 15
df['city'] = ['cbe' , 'chennai' , 'chennai' , 'cbe' , 'saidapet']
print(df)
print("\n")

dirty = df.groupby('subject')
print(dirty['marks'].mean())
print("\n")

cha = df.groupby('city')['marks'].agg(['min' , 'max'])
print(cha)
print("\n")

shae = df.groupby('subject')['marks'].agg(['mean' , 'count' , 'max'])
print(shae)
print("\n")





    


