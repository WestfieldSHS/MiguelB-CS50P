camelCase = input("Input a variable in camelCase: ")
# prepares a variable
snake = ""
for char in camelCase:
    # determines whether to add an underscore before each now-lower_case letter
    # before adding it to the prepped variable
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char
print(snake)