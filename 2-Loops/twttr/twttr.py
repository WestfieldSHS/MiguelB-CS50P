vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
msg = input("Message: ")
for letter in msg:
    if letter in vowels:
        msg = msg.replace(letter, "")
print(msg)