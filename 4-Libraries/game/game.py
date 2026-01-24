import random

def main():
    maxima = positive_checker("Input")
    number_to_guess = random.randint(1, maxima)
    guess_counter = guess_checker(number_to_guess)
    print(f"It took {guess_counter} guesses.")

def positive_checker(word):
    positive = False
    while positive == False:
        n = int(input(f"{word} an integer greater than 0: "))
        if n > 0:
            positive = True
    return n

def guess_checker(number_to_guess):
    guessing = True
    guess_counter = 0
    while guessing == True:
        guess = positive_checker("Guess")
        guess_counter += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        elif guess == number_to_guess:
            print("That's correct!")
            guessing = False
    return guess_counter

main()