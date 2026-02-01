grocery_list = []

while True:
    try:
        item = input("What item would you like to add to the grocery list? ")
    except EOFError:
        break
    grocery_list.append(item)

unique_list = set(grocery_list) # set() removes duplicate items in a list

# cycles thru unique_list while counting grocery_list
for item in unique_list:
    count = grocery_list.count(item)
    print(f"[{count}] {item}")
