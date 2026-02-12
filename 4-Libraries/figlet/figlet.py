import random, sys
from pyfiglet import Figlet
figlet = Figlet()
font_list = figlet.getFonts()
decision = False

text = input("Text: ")
font_decision = input("Do you want to set the font? Y/N: ")
while decision == False:
    if font_decision == "Y":
        f = input("What font do you want? ").lower()
        if f in font_list:
            decision = True
        else:
            print("Invalid Usage")
            sys.exit()
    elif font_decision == "N":
        f = random.choice(font_list)
        decision = True
f = Figlet(font=f)
print(f.renderText(text))