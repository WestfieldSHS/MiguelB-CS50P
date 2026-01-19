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
    hour, minute = time.split(" ")
    hour = float(hour)
    minute = float(minute)/60
    return hour + minute

main()