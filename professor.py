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


if __name__ == "__main__":
    main()