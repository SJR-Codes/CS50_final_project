"""
* CS50P Problem Set 4
* Adieu, Adieu
* by Samu Reinikainen 25.07.2022
"""
import inflect

p = inflect.engine()

def main():
    #print("Name: ")
    names = say_adieu(get_input(""))

def get_input(prompt):
    names = []
    while True:
        try:
            names.append(input(prompt).lower().title())
        except EOFError:
            return names

def say_adieu(names):
    adieu = p.join(names)

    print("Adieu, Adieu, to " + adieu)

main()