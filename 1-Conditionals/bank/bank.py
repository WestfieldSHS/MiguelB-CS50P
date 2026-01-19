greeting = input("Enter a greeting: ")
greeting = greeting.strip()
greeting = greeting.lower()
if greeting == "hello":
    output = "0"
elif greeting[0] == "h":
    output = "20"
else:
    output = "100"
print(f"Here is ${output}.")