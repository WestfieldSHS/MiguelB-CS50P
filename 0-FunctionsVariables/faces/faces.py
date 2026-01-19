message = input("Message: ")
if ":(" in message:
    message = message.replace(":(", "🙁")
if ":)" in message:
    message = message.replace(":)", "🙂")
print(message)