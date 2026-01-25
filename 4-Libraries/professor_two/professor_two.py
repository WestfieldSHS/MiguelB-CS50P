import random

level_list = ["1", "2", "3"]

def main():
    level = get_level()
    completed_questions = generate_level(level)
    results(completed_questions)

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
    question = 1
    completed_questions = 0
    for i in range(10):
        print()
        attempt_check = True
        attempt_count = 0
        x, y = random.randint(1, maxima), random.randint(1, maxima)
        program_ans = x + y
        while attempt_check == True:
            attempt_count += 1
            user_answer = int(input(f"Q{question}. What is {x}+{y}? "))
            if user_answer == program_ans:
                completed_questions += 1
                attempt_check = False
            else:
                print("EEE")
            if attempt_count == 3:
                attempt_check = False
        question += 1
    return completed_questions
    
def results(completed_questions):
    print()
    print(f"You got {completed_questions}/10 questions correct!")

main()