"""
* CS50P Problem Set 0
* Making Faces
* by Samu Reinikainen
"""

def main():
    #get users input
    userinput = input("Enter your input, please: ")

    #print user input with faces
    print(convert(userinput))


def convert(strtoconv):

    convertedstr = strtoconv.replace(":)", "🙂")
    convertedstr = convertedstr.replace(":(", "🙁")

    return convertedstr

main()