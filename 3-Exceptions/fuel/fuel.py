# didnt use functions - wasnt bothered
while True:
    fraction = input("Input a fraction (x/y): ")
    fraction = fraction.replace("/", " ")
    x, y = fraction.split(" ")
    try:
        x, y = int(x), int(y) # you can do this apparently
        try: # are u allowed to indent try/except like this
            decimal = 100*(x/y) # creates a decimal from the fraction
        except ZeroDivisionError:
            print("Error! Denominator cannot be equal to zero.")
            continue
    except ValueError:
        print("Error! Please input integers.")
    else:
        if 0 < x < y:
            break
        else:
            print("Numerator must be positive.")

if decimal >= 99:
    print("Your fuel tank is fuel.")
elif decimal <= 1:
    print("Your fuel tank is empty.")
else:
    print(f"You have {decimal}% remaining in your fuel tank.")