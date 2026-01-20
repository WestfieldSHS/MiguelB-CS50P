nutrition = {
    "Apple": 130,
    "Avocado": 50
}

fruit = input("What fruit would you like too see the nutrition of? ")
if fruit in nutrition:
    print(f"{fruit} has {nutrition[fruit]} calories.")
else:
    print("I don't know about that one.")