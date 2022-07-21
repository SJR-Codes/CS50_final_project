"""
* CS50P Problem Set 0
* Einstein
* by Samu Reinikainen
"""

def main():
    #get users input
    mass = int(input("Give mass in kg's, please: "))

    #calculate energy and print
    print(e2mc(mass))


def e2mc(mass):
    c = 300000000

    e = mass * pow(c, 2)

    return e

main()