name_list = []

while True:
    try:
        name = input("Input a name: ")
        name_list.append(name)
    except EOFError:
        break

length = len(name_list)
n = 0

while True:
    for name in name_list:
        print(name_list[n:])
        n += 1
    break