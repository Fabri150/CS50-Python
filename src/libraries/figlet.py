from pyfiglet import Figlet
import sys
import random

if len(sys.argv) == 1:
    text = input("Input: ")
    f = Figlet(font=random.choice(Figlet().getFonts()))
    print(f.renderText(text))
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in Figlet().getFonts()):
    text = input("Input: ")
    f = Figlet(font=sys.argv[2])
    print(f.renderText(text))
else:
    sys.exit("Invalid usage")