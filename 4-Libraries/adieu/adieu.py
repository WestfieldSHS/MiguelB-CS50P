name_list = []
string = "Adieu Adieu to "

while True:
    try:
        name = input("Input a name: ")
        name_list.append(name)
    except EOFError:
        break

length = len(name_list)
n = 0

for name in name_list:
    if name == name_list[0]:
        string = string + f"{name}"
    if name == name_list[-1]:
        string = string + f""
    print(string)