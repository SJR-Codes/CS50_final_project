"""
* CS50P Problem Set 4
* Little Professor
* by Samu Reinikainen 25.07.2022
"""

import sys
import random

def main():
    level = get_level()

    rint = generate_integer(level)

    print(rint)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if 3 >= level > 0:
                return level

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