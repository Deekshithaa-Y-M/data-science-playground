print("Day 21 - Introduction to Matplotlib - Line & Bar Plots")

from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.show()

#bar chart
names =  ['ajay' , 'bala', 'charan']
scores=[85,90,88]
plt.bar(names, scores)
plt.show()

#tasks for day 21
import numpy as np
days = np.random.randint(1,10,10)
print("The days are:" , days)
print("\n")

temparature = np.random.randint(35,75,10)
print("temperature values are: ", temparature)
print("\n")

plt.plot(days,temparature)
plt.show()

names =  ['aneesh' , 'balu', 'chithra']
scores=[85,90,36]
plt.bar(names, scores,color='orange')
plt.show()
plt.bar(scores, names,  color = 'purple')
plt.show()
