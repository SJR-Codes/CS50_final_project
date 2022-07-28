"""
* CS50P Problem Set 7
* Regular, um, Expressions
* by Samu Reinikainen 28.07.2022
"""

import re
import sys

def main():
    print(count(input("Text: ")))
    #print(count("Regular, um, um, Expressions"))


def count(s):
    p = r"(?:\W(um)\W)"
    if m := re.findall(p, s, flags=re.IGNORECASE):
        #print(m)
        return len(m)

    return 0


if __name__ == "__main__":
    main()