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
    # ensures that no matter what format used, the result is MM DD YYYY
    anno_domini = anno_domini.replace("/", " ")
    anno_domini = anno_domini.replace(", ", " ")
    month, day, year = anno_domini.split(" ")
    if month in month_list: 
        # if month is a word, it becomes the index (number) of its location in the month_list
        # one is then added to it to counteract the fact that indexes start at 0 and not 1
        # list.index makes a str into a int whilst list[num] makes an int into a str (basically)
        month = month_list.index(month) + 1
    # turns day into a str, and year as well so they are all ints and its nicer that way
    # even tho month is already an int thru the indexing, that is only applied if it was originally a WORD and not a str-number like "12"
    month, day, year = int(month), int(day), int(year)
    # verifies if the numbers are appropriate.
    if 1 <= month <= 12:
        if 1 <= day <= 31:
            format = True
print(f"{day}/{month}/{year}")

# if we gotta print the month in word form:
#     if month in numbers:
#        month = int(month) - 1
#        month = month_list[month]