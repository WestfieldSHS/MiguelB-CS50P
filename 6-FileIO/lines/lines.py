try:
    py = input("Input a path to the python file: ")
    count = 0
    with open(py, "r") as file:
        for line in file:
            if line:
                count += 1
    print(f"The file has {count} lines.")
except FileNotFoundError:
    print("File Not Found")