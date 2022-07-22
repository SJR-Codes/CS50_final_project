"""
* CS50P Problem Set 1
* Meal Time
* by Samu Reinikainen 22.07.2022
"""


def main():
    utime = input("What time is it? ").strip()

    ctime = convert(utime)

    if 8 >= ctime >= 7:
        print("Breakfast")
    elif 13 >= ctime >= 12:
        print("Lunch")
    elif 19 >= ctime >= 18:
        print("Dinner")
    else:
        pass

def convert(time):
    tmp = time.split(":")

    return float(int(tmp[0]) + (int(tmp[1])/60))


if __name__ == "__main__":
    main()