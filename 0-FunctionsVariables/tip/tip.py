def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    # :.2f -> float to two decimal points
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # gets rid of the dollar sign
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):
    # gets rid of the percent sign and then divides by 100 to create a fraction
    p = p.replace("%", "")
    return float(p)/100

main()