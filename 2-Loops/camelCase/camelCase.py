#get a string, make it lowercase, seperate words in string with _, 
camelCase = input("Input a variable in camelCase: ")
snake = ""
for char in camelCase:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char
print(snake)