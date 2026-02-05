# i don't know how figlet works.
import random
from pyfiglet import Figlet
figlet = Figlet()
font_list = figlet.getFonts()

decision = False

text = input("Text: ")
font_decision = input("Do you want to set the font? Y/N: ")
while decision == False:
    if font_decision == "Y":
        f = input("What font do you want? ").lower()
        decision = True
    elif font_decision == "N":
        f = random.choice(font_list)
figlet.setFont(font=f)
print(figlet.renderText(text))