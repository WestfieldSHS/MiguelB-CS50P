filename = input("File name: ")
filename = filename.lower()
# sees if the variable.. ends with.. any of the items in the brackets
if filename.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")) == True:
    # checks to see if its .jpeg which has a different len
    if filename.endswith(".jpeg"):
        num = 5
    else:
        num = 4
    #prints the last n characters (which would always be the file type). 
    # if the colon was absent, it would only print the nth character to the end.
    print(filename[-num:])
else:
    print("application/octet-stream")