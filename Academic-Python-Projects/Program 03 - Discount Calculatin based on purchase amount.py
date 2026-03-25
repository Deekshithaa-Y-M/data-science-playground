#Program 3

''' A store offers a discount based on the total purchase amount:
 If the total amount is above ₹10,000, the discount is 20%.
 If the amount is between ₹5,000 and ₹10,000, the discount is 10%.
 If the amount is below ₹5,000, there is no discount.
Write a program to calculate the final amount after the discount'''

# Input the total amount
total_amount = float(input("Enter the total purchase amount: "))
if total_amount > 10000:
    discount = 0.20 * total_amount
elif total_amount >= 5000:
    discount = 0.10 * total_amount
else:
    discount = 0
    
final_amount = total_amount - discount
print("The final amount after discount is: ", final_amount)
