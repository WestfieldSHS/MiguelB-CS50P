price_check = False
price_match = 50
accepted_coins = ["25c", "10c", "5c"]

while price_check == False:
    insert_coin = input("Insert a coin (25c, 10c, 5c): ")
    if insert_coin in accepted_coins:
        insert_coin = int(insert_coin.replace("c", ""))
        price_match = price_match - insert_coin
        print(f"Price remaining: {price_match}")
        if price_match <= 0:
            price_check = True
    else:
        print("Input an accepted coin.")
print("Here's your coke.")