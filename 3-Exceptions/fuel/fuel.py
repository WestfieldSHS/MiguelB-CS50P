fraction = input("Input a fraction (x/y): ")
fraction = fraction.replace("/", " ")
x, y = fraction.split(" ")
x = int(x)
y = int(y)
decimal = 100*(x/y)
if decimal >= 99:
    print("Your fuel tank is fuel.")
elif decimal <= 1:
    print("Your fuel tank is empty.")
else:
    print(f"You have {decimal}% remaining in your fuel tank.")