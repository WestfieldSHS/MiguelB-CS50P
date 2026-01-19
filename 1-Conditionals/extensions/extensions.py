filename = input("File name: ")
filename = filename.lower()
if filename.endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")) == True:
    num = 4
    print(filename[-num:])
else:
    print("application/octet-stream")