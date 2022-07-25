"""
* CS50P Problem Set 4
* Guessing Game
* by Samu Reinikainen 25.07.2022
"""

import sys
import random as r

def main():
    level = get_input("Level: ")

    rnum = r.randint(1,level)

    get_guess(rnum)

def get_input(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
        except ValueError:
            pass
        
def get_guess(rnum):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess > rnum:
                    print("Too large!")
                elif guess < rnum:
                    print("Too small!")
                else:
                    sys.exit("Just right!")

        except ValueError:
            pass


main()