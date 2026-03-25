print("Day 5 - Numpy - advance indexing and masking")
import numpy as np

avm = np.array([10,20,30,40,50])

mask = avm > 25 # Masking is useful for selecting specific data points!
print(avm[mask])
print("\n")

#exercise 1
wil = np.array([1,2,63,94,51,6,7,88,99,9,8,7,6,5,4])

fre = wil > 50
print(wil[fre])
print("\n")

#fancy indexing
bal = np.array([10,20,30,40,50])
indices = [0,2,4]
print(bal[indices])
print("\n")

#exercise 2
qui = np.array([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40])
wee = [2,5,8,11,14]
print(qui[wee])
print("\n")

#setting values using masking&indexing
lac = np.array([10,20,30,40,50])
lac[lac>30] = 0
print(lac)
print("\n")

#exercise 3
ran = np.random.randint(1,51,10)
print(ran)
print("\n")

ran[ran % 2 != 0] = -1
print(ran)


