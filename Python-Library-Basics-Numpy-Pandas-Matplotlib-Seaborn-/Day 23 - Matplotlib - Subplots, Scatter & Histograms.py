print("Day 23 - Matplotlib - subplots, scatter, histogram")

#subplots - 2 or more charts side by side

from matplotlib import pyplot as plt

plt.subplot(1,2,1)
plt.plot([1,2,3] , [4,5,6])
plt.title("Left plot")

plt.subplot(1,2,2)
plt.bar(['a', 'b' , 'c'],[3,2,5])
plt.title("Right Plot")
plt.tight_layout()
plt.show()

x = [5, 7, 8, 7, 2]
y = [99, 86, 87, 88, 100]

plt.scatter(x, y, color='red')
plt.show()

marks = [80,85,70,90,85,88,70,95,65]
plt.hist(marks, bins=5)
plt.show()

#tasks for day 23
plt.subplot(1,2,1)
plt.plot([5,6,7], [8,9,10])
plt.title("FIRST")

plt.subplot(1,2,2)
plt.bar(['kiru' , 'tharu' , 'thuru'] , [10,11,9])
plt.title("SECOND")

plt.tight_layout()
plt.show()

h = [155,160,165,170,175]
w = [50,52,54,56,58]
plt.grid(True)
plt.scatter(h, w, color = 'cyan')
plt.xlabel("height")
plt.ylabel("weight")
plt.show()

plt.figure(figsize=(8,5))
mark = [99, 80, 76, 53, 45, 34,33,95, 97,100]
plt.hist(mark, bins=5)
plt.show()
