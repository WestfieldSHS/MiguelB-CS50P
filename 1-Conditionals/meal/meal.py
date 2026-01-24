def main():
    time = input("Time: ")
    number = convert(time)
    if 7 <= number <= 8:
        print("It's breakfast time.")
    elif 12 <= number <= 13:
        print("It's lunch time.")
    elif 18 <= number <= 19:
        print("It's dinner time.")

def convert(time):
    time = time.replace(":", " ")
    # sets the variables to the split list's variables
    hour, minute = time.split(" ")
    hour = float(hour)
    # converting minutes to hours means dividing by 60
    minute = float(minute)/60
    # returns the sum (e.g 7.5)
    return hour + minute

main()