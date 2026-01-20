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
ordering = True

while ordering:
    try:
        order = input("What item would you like? ")
    except EOFError:
        ordering = False
        break
    price = menu[order]
    price_list.append(price)
    
total_price = sum(price_list)
print(f"The total price of your order is {total_price}.")

