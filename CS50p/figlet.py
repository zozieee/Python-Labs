from pyfiglet import Figlet
import random
import sys

figlet=Figlet()

if len(sys.argv)==1:
    randFont=True
elif len(sys.argv) == 3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
    randFont=False
    try:
        figlet.setFont(font=sys.argv[2])

    except:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

s=input("Input: ")

if randFont==True:
    fontlist=figlet.getFonts()
    n=random.randrange(0, len(fontlist))
    figlet.setFont(font=fontlist[n])
    print(figlet.renderText(s))

elif randFont==False:
    try:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
    except:
        print("Invalid usage")
        sys.exit(1)