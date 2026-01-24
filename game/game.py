import random

def main():
    maxima = positive_checker("Input")
    number_to_guess = random.randint(1, maxima)
    guess = positive_checker("Guess")
    

def positive_checker(word):
    positive = False
    while positive == False:
        n = int(input(f"{word} an integer greater than 0: "))
        if n > 0:
            positive = True
    return n

main()