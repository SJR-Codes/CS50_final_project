"""
* CS50P Problem Set 3
* Fuel Gauge
* by Samu Reinikainen 24.07.2022
"""

def main():
    x = (get_input("Enter fraction (x/y, ie. 3/4): "))
    print(fract_to_gauge(x))

def get_input(prompt):
    while True:
        x = check_input(input(prompt))
        #print(x)
        if x != False:
            return x

def check_input(fract):
    if(fract.count("/") == 1):
        fract = fract.split("/")
    else:
        return False

    try:
        x = int(fract[0])
        y = int(fract[1])
    except ValueError:
        #print("Value Error: Not valid fraction!")
        return False

    if y <= 0 or x < 0 or x > y:
        #print("Zero or Negative Number Error: Not valid fraction!")
        return False

    return fract


def fract_to_gauge(fract):
    #convert fract to gauge, ie. 3/4 = 75%
    res = round(int(fract[0]) / int(fract[1]) * 100)

    if res <= 1:
        res = "E"
    elif res >= 99:
        res = "F"
    else:
        res = str(res) + "%"

    return res

main()