"""
* CS50P Problem Set 4
* Little Professor
* by Samu Reinikainen 25.07.2022
"""

import sys
import random

def main():
    #print("Level: ", end="")
    level = get_level("Level: ")
    guestions = generate_guestions(level)
    score = ask_guestions(guestions)

    print(score)

    sys.exit()

def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
        except ValueError:
            continue
        else:
            if 3 >= level > 0:
                break

    return level

def generate_integer(level):
    if 3 >= level > 0:
        return random.randint(1, (10**level)-1)
    else:
        raise ValueError

def generate_guestions(level):
    guestions = []
    for x in range(10):
        guestions.append(generate_guestion(level))

    return guestions

def generate_guestion(level):
    x = generate_integer(level)
    y = generate_integer(level)

    return str(x) + " + " + str(y)

def ask_guestions(guestions):
    score = 0
    for guest in guestions:
        correct = False
        tries = 0
        while tries < 3:
            try:
                answr = int(input(guest + " = "))
                if answr == eval(guest):
                    score += 1
                    correct = True
                    break
                else:
                    tries +=1
                    print("EEE")
            except ValueError:
                tries +=1
                print("EEE")
        if correct == False:
            print(guest + " = " + str(eval(guest)))

    return score

if __name__ == "__main__":
    main()