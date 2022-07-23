"""
* CS50P Problem Set 2
* Vanity Plates
* by Samu Reinikainen 23.07.2022
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #“All vanity plates must start with at least two letters.”
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    #“Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”
    #“No periods, spaces, or punctuation marks are allowed.”

    if v_amount(s) and v_start(s) and v_chars(s) and v_nums(s) and v_nozero(s):
        return True

    return False


def v_start(s):
    #check that first two chars are letters
    if s[0].isalpha() and s[1].isalpha():
        return True
    return False

def v_amount(s):
    #check that string len is 2-6
    return 6 >= len(s) >= 2

def v_chars(s):
    #check that string has only alphanumeric chars
    return s.isalnum()

def v_nums(s):
    #check that there's numbers only at the end
    if(s.isalpha()):
        return True

    has_d = False
    for x in s:
        if x.isdigit():
            has_d = True
        if x.isalpha and has_d:
            return False

    return True

def v_nozero(s):
    #check that numbers dont start with zero
    if(s.isalpha()):
        return True

    for x in s:
        if x.isdigit() and int(x) > 0:
            return True
        elif x.isdigit() and int(x) == 0:
            return False

main()