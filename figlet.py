"""
* CS50P Problem Set 4
* Frank, Ian and Glen’s Letters
* by Samu Reinikainen 25.07.2022
"""

import sys
import random as r
from pyfiglet import Figlet

figlet = Figlet()
#You can then get a list of available fonts with code like this:
fonts = figlet.getFonts()
#print(fonts)

if len(sys.argv) == 1:
    f = r.choice(fonts)
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        f = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

#You can set the font with code like this, wherein f is the font’s name as a str:
figlet.setFont(font=f)

#And you can output text in that font with code like this, wherein s is that text as a str:
print(figlet.renderText(input("What to print: ")))

