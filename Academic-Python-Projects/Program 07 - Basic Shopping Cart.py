#Program 7 - Basic Shopping Cart

# (a) Create a list with at least 10 different item names
shopping_cart = ["Milk", "Bread", "Eggs", "Rice", "Sugar", "Salt", "Butter",
"Cheese", "Tomatoes", "Potatoes"]

# (b) Remove an item from the cart
item_to_remove = "Sugar"
if item_to_remove in shopping_cart:
    shopping_cart.remove(item_to_remove)
    print(f"'{item_to_remove}' has been removed from the cart.")
else:
    print(f"'{item_to_remove}' is not in the cart.")
      
# (c) Add a new item to the cart
item_to_add = "Apples"
shopping_cart.append(item_to_add)
print(f"'{item_to_add}' has been added to the cart.")

# (d) Display the total number of items in the cart
print("\nTotal items in the cart:", len(shopping_cart))

# (e) Print the list of items in alphabetical order
print("\nItems in alphabetical order:", sorted(shopping_cart))

# (f) Search for an item in the cart
item_to_search = "Milk"
if item_to_search in shopping_cart:
    print(f"'{item_to_search}' is available in the cart.")
else:
    print(f"'{item_to_search}' is not in the cart.")

# Display the final cart
print("\nCurrent Shopping Cart:", shopping_cart)
