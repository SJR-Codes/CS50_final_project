"""
* CS50P Problem Set 2
* Coke Machine
* by Samu Reinikainen 23.07.2022
"""

def main():
    uinp = input("Say what? ")

    print(twitify(uinp))


def twitify(uinp):
    #remove vowels (A, E, I, O, and U)
    rem_vowls = ["A","E","I","O","U"]
    ret = ""

    for x in uinp:
        if x.upper() not in rem_vowls:
            ret += x

    return ret

main()