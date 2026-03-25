#Program 8 - To find the Second Largest element in the list.

# declaring the list
L1 = []
n=int(input("Enter the number of elements to enter in the list: "))
for i in range (n):
    x = int(input("Enter the element: "))
    L1.append(x)
    
def second(L1):
    L1.sort() # sorting the list
    print("The second largest element of the list is: ", L1[-2]) # printing the element of the second last index
second(L1) # calling the function
