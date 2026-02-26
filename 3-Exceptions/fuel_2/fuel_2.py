def main():
    while True:
        x, y = input_fraction()
        x, y = integer_convert(x, y)
        decimal = decimal_convert(x, y)
        decimal_check(decimal)
        read_fuel(decimal)

def input_fraction():
    fraction = input("Input a fraction (x/y): ")
    fraction = fraction.replace("/", " ")
    x, y = fraction.split(" ")
    return x, y

def integer_convert(x, y):
    try:
        x, y = int(x), int(y) # you can do this apparently
    except ValueError:
            print("Error! Please input integers.")
    return x, y

def decimal_convert(x, y):
    try:
        decimal = 100*(x/y) # creates a decimal from the fraction
    except ZeroDivisionError:
        print("Error! Denominator cannot be equal to zero.")
        main()
    else:
        return decimal

def decimal_check(decimal):
    if decimal < 0:
        print("Decimal must be positive")
        main()
    else:
        pass

def read_fuel(decimal):
    if decimal >= 99:
        print("Your fuel tank is fuel.")
    elif decimal <= 1:
        print("Your fuel tank is empty.")
    else:
        print(f"You have {decimal}% remaining in your fuel tank.")

main()