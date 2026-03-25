#day 22

print("Day 22 - Matplotlib - Plot Customization: Title, Colors, Labels")

from matplotlib import pyplot as plt
import numpy as np

x = np.random.randint(1,20,10)
print(x)
print("\n")

y = np.random.randint(1,50,10)
print(y)
print("\n")

plt.plot(x,y, color='green', marker='o' , linestyle = '--' )
plt.title("Growth over time")
plt.xlabel("Day")
plt.ylabel("Value")
plt.show()

#tasks for day 22

a = [1,2,3,4,5,6,7,8,9,10]
b = [99,101,105,112,113,119,205,206,206.5,215]
plt.plot(a , b , color = 'red' , marker = 'o' , linestyle = ':')
plt.title("Number of swans a student can make")
plt.xlabel("Roll No.")
plt.ylabel("No. of Students")
plt.show()

colors = ['skyblue' , 'lightcoral' , 'lightgreen' , 'lightyellow']
plt.bar(a , b, color = colors, width = 0.6)
plt.title("Number of swans a student can make")
plt.xlabel("Roll No.")
plt.ylabel("No. of Students")
plt.show()
