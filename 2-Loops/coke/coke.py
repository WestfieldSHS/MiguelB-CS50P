price_check = False
price_match = 50
accepted_coins = ["25c", "10c", "5c"]

# while loop
while price_check == False:
    insert_coin = input("Insert a coin (25c, 10c, 5c): ")
    if insert_coin in accepted_coins:
        # gets rid of cent before turning it into an integer
        insert_coin = int(insert_coin.replace("c", ""))
        price_match = price_match - insert_coin
        if price_match <= 0:
            change = price_match * -1
            price_check = True
        else:
            print(f"Price remaining: {price_match}")
    else:
        print("Input an accepted coin.")
print("Here's your coke.")
if change: 
    print(f"Here is your change: {change}c.")