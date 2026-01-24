# test dictionary because I didnt wanna add all the fruits
nutrition = {
    "Apple": 130,
    "Avocado": 50
}

fruit = input("What fruit would you like too see the nutrition of? ")
if fruit in nutrition:
    # dict[key] is how to call the key of a certain value in a dictionary
    # in this instance, fruit is determined by the programme to be the variable pertaining to the dict's value
    print(f"{fruit} has {nutrition[fruit]} calories.")
else:
    print("I don't know about that one.")