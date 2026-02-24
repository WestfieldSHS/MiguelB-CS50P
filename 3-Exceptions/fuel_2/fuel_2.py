def main():
    while True:
        x, y = input_fraction()
        x, y = integer_convert(x, y)
        decimal = decimal_convert(x, y)
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
    if 0 < x < y:
        return x, y

def decimal_convert(x, y):
    try: # are u allowed to indent try/except like this
        decimal = 100*(x/y) # creates a decimal from the fraction
    except ZeroDivisionError:
        print("Error! Denominator cannot be equal to zero.")
    else:
        return decimal

def read_fuel(decimal):
    if decimal >= 99:
        print("Your fuel tank is fuel.")
    elif decimal <= 1:
        print("Your fuel tank is empty.")
    else:
        print(f"You have {decimal}% remaining in your fuel tank.")

main()