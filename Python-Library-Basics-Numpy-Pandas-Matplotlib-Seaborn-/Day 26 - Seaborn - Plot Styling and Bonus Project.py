#mini project and day 26
print("Day 26 - Plot Styling + Bonus Project")

import seaborn as sns
from matplotlib import pyplot as plt

sns.set_style("darkgrid")

sns.set_palette("pastel")

df = sns.load_dataset('tips')

sns.catplot(x='day' , y = 'tip' , hue = 'sex' , kind= 'bar' , data = df)

plt.show()

#task for day 26

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)

sns.barplot(x='day' , y='total_bill' , data = df)

plt.title('Total bill by day')

plt.subplot(2, 2, 2)

sns.boxplot(x='smoker', y='tip', data=df)

plt.title('Tip by Smoker')

plt.subplot(2, 2, 3)

sns.countplot(x='time', data=df)

plt.title('Lunch vs Dinner Count')

plt.tight_layout()

plt.savefig("tips data visualization.png") #this command should be added before plt show

plt.show()
