answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
answer.lower()
if "forty-two" == answer:
    print("Yes!")
elif "42" == answer:
    print("Yes!")
else:
    print("No.")