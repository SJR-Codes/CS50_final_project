"""
* CS50P Problem Set 7
* Response Validation
* by Samu Reinikainen 28.07.2022
"""

from validator_collection import validators, errors

def main():
    print(check(input("What's your email address? ").strip()))
    #print(check("ad@ad.fi"))


def check(e):

    try:
        if validators.email(e, allow_empty = False):
            return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()