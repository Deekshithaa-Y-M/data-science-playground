print("Day 24 - Seaborn - Pro Charts with the least code!")

#day 24

import seaborn as sns
from matplotlib import pyplot as plt

sns.set_style("dark")

sns.set_palette("coolwarm")

df = sns.load_dataset('tips')

print(df.head())

sns.lineplot(x='total_bill' , y = 'tip' , data = df)

plt.title("Lineplot - Bill vs Tip")

plt.show()

sns.barplot(x='day' , y='total_bill', data = df)

plt.title("Average Bill per Day")

plt.show()

#tasks for day 24
df = sns.load_dataset('penguins')
print(df.head(5))

sns.lineplot(x='species' , y = 'flipper_length_mm' , data = df)

plt.title("species vs flipper length")

plt.xlabel("species")

plt.ylabel("flipper length")

plt.show()

sns.barplot(x = 'island' , y = 'bill_depth_mm' , data = df)

plt.xlabel("island")

plt.ylabel("bill_depth_mm")

plt.title("island vs bill depth")

plt.show()
