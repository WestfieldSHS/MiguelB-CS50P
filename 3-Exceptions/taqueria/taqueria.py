menu = {
		"Baja Taco": 4.25,
		"Burrito": 7.50,
		"Bowl": 8.50,
		"Nachos": 11.00,
		"Quesadilla": 8.50,
		"Super Burrito": 8.50,
		"Super Quesadilla": 9.50,
		"Taco": 3.00,
		"Tortilla Salad": 8.00,
	}

price_list = []
order_list = []
ordering = True

print(menu)
print()
while ordering:
    # try and except loop
    try:
        order = input("What item would you like? ")
        # adds the order to the designated list immediately
        order_list.append(order)
    except EOFError: # error that appears when you use ctrl+z (on windows), ctrl+d (on mac)
        ordering = False # ends the loop
        break # terminates it as well
    
for order in order_list:
	price = menu[order] # gets the key of the value in the dict
	price_list.append(price) # immediately appends it to a new list
    
total_price = sum(price_list) # sum method adds ints in a list
print(f"The total price of your order is {total_price}.")

