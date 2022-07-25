"""
* CS50P Problem Set 4
* Little Professor
* by Samu Reinikainen 25.07.2022
"""

import sys
import random

def main():
    #print("Level: ", end="")
    while True:
        level = get_level("Level: ")
        try:
            level = int(level)
            generate_integer(level)
            break
        except ValueError:
            continue

    sys.exit("6 + 6 = ")

def get_level(prompt):
    return input(prompt)

def generate_integer(level):
    if 3 >= level > 0:
        match level:
            case 1:
                start = 0
            case 2:
                start = 10
            case 3:
                start = 100
        return random.randint(start, (10**level)-1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()