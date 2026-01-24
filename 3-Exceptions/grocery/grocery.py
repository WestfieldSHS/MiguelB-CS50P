# uncompleted

grocery_list = []

while True:
    try:
        item = input("What item would you like to add to the grocery list? ")
    except EOFError:
        break
    grocery_list.append(item)

from collections import Counter
counts = Counter(grocery_list)

for item, count in counts:
    print(f"{count}: {item}")