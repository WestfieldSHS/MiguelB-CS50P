import random

level_list = ["1", "2", "3"]

def main():
    level = get_level()
    generate_level(level)

def get_level():
    while True:
        level = input("Input a level (1-3): ")
        if level in level_list:
            return level
        
def generate_level(level):
    if level == "1":
        maxima = 10
    elif level == "2":
        maxima = 20
    elif level == "3":
        maxima = 50
#    questioning = True
#    while questioning == True:
#        x, y = random.randint(1, maxima), random.randint(1, maxima)
#        acc_answer = x+y
#        attempt = 1
#        while attempt < 3:
#            user_answer = print(f"Q{question}. What is {x}+{y}? ")
#            if user_answer == acc_answer:
#                break
#            else:
#                attempt += 1

main()
