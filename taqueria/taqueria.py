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

order_list = []

while True:
    try:
        order = input("What item would you like? ")
    except EOFError:
        break
order_list.append(order)
for order in order_list:
    price = menu[order]
    
total_price = 0
for price in price_list:
    total_price = total_price + price
print(f"The total price of your order is {total_price}.")

