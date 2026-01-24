month_list = [
		"January",
		"February",
		"March",
		"April",
		"May",
		"June",
		"July",
		"August",
		"September",
		"October",
		"November",
		"December",
]

numbers = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
]

# you could also just merge the two lists but i dont know if were allowed to do that in this question.

format = False

while format == False:
    anno_domini = input("Date [(MM/DD/YYYY) or (Month Day, Year)? ")
    anno_domini = anno_domini.replace("/", " ")
    anno_domini = anno_domini.replace(", ", " ")
    month, day, year = anno_domini.split(" ")
    if month in month_list:
        month = month_list.index(month) + 1
    month, day, year = int(month), int(day), int(year)
    if 1 <= month <= 12:
        if 1 <= day <= 31:
            format = True
print(f"{day}/{month}/{year}")

# if we gotta print the month in word form:
#     if month in numbers:
#        month = int(month) - 1
#        month = month_list[month]