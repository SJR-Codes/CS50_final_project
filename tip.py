"""
* CS50P Problem Set 0
* Einstein
* by Samu Reinikainen
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#conv str to float, removing $-sign
def dollars_to_float(d):
    d = float(d.replace("$", ""))

    return d

#conv str to float, removing %-sign
def percent_to_float(p):
    p = float(p.replace("%", "")) / 100

    return p

main()