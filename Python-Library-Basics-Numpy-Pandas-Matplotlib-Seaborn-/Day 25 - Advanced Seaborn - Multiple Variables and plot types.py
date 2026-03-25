#day 25
print("Day 25 - Advanced Seaborn - Multiple Variables & Plot Types")

import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset('tips')

sns.countplot(x='day' , data=df)

plt.title("How many entries per day")

plt.show()

sns.boxplot(x='day' , y ='total_bill' , data = df)

plt.title("Bill Distribution per day")

plt.show()

sns.barplot(x='day' , y='tip' , hue='sex' , data = df)

plt.title("Average tip by gender and day")

plt.show()

#tasks for day 25

df = sns.load_dataset('titanic')

print(df.head(6))

sns.countplot(x='fare', data = df)

plt.show()

sns.boxplot(x = 'age' , y = 'survived' , data = df)

plt.show()

sns.barplot(x='age' , y='survived' , hue = 'embarked', data = df)

plt.show()
