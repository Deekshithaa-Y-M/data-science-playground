print("Day 18 - Pandas - Working with dates")
#day 18
import pandas as pd

df = pd.DataFrame({
    'name': ['ajay', 'bala', 'charan'],
    'date_joined': ['2023-01-10', '2022-12-15', '2023-02-20']
})

df['date_joined'] = pd.to_datetime(df['date_joined'])
print(df.dtypes)
print("\n")

df['year'] = df['date_joined'].dt.year

df['month'] = df['date_joined'].dt.month

df['weekday'] = df['date_joined'].dt.day_name()
print(df)
print("\n")

#task for day 18

df = pd.DataFrame({
    'name' : ['geronimo' , 'stilton' , 'thea' , 'grace' , 'lucy'],
    'joining_date' : ['2019-01-12' , '2018-01-05' , '2022-05-03' , '2022-04-10' , '2024-07-11']
})

df['joining_date'] = pd.to_datetime(df['joining_date'])

df['year'] = df['joining_date'].dt.year

df['month'] = df['joining_date'].dt.month

df['day of joining'] = df['joining_date'].dt.day_name()

a = df.sort_values(by = 'joining_date') #we can sort the values only after adding all necessary columns, otherwise it gives the wrong output
print(a)




