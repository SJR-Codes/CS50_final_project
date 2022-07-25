"""
* CS50P Problem Set 4
* Little Professor
* by Samu Reinikainen 25.07.2022
"""

import sys
import random

def main():
    level = get_level("Level: ")

def get_level(prompt):
    while True:
        level = input(prompt)
        try:
            level = int(level)
        except ValueError:
            continue
        else:
            if 3 >= level > 0:
                return level


if __name__ == "__main__":
    main()