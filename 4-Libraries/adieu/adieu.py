name_list = []

while True:
    try:
        name = input("Input a name: ")
        name_list.append(name)
    except EOFError:
        break

n = len(name_list)

while True:
    break