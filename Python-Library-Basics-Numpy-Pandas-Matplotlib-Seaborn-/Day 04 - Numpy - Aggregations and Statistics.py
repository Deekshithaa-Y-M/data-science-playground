print("Day 4 - Numpy - Aggregations and Statistics")
import numpy as np

arr = np.array([1,2,3,4,5])

print(np.sum(arr))  #sum of all elements
print(np.mean(arr)) #average
print(np.min(arr)) #minimum
print(np.max(arr)) #maximum
print(np.std(arr)) #standard deviation

#exercise 1
ski = np.array([10,20,30,40,50,60,70,80,90,100])
print(np.sum(ski))
print(np.mean(ski))
print(np.min(ski))
print(np.max(ski))
print(np.std(ski))

#aggregations and multi-dimensional arrays
mat = np.array([[1,2,3],
                [4,5,6]])
print(np.sum(mat, axis=0))
print(np.sum(mat, axis=1))

#exercise 2
vap = np.array([[4,5,6,7],
                [1,2,3,4],
                [5,6,7,8],
                [9,9,9,9]])
print(np.sum(vap, axis = 1))
print(np.mean(vap, axis = 0))

flex = np.array([1,3,5,7,9])
print(np.median(flex))  # 5 (Middle value)
print(np.percentile(flex, 50))  # 50th percentile (Median)
print(np.percentile(flex,90)) # 90th percentile

#exercise 3
pro = np.array([1,22,3,4,5,6,7,8,9,10,11,2,3,4,5])
print(np.median(pro))
print(np.percentile(pro, 25))
print(np.percentile(pro,75))
