"""
* CS50P Problem Set 1
* Meal Time
* by Samu Reinikainen 22.07.2022
"""


def main():
    utime = input("What time is it? ").strip()

    ctime = convert(utime)

    if 8 >= ctime >= 7:
        print("breakfast time")
    elif 13 >= ctime >= 12:
        print("lunch time")
    elif 19 >= ctime >= 18:
        print("dinner time")
    else:
        pass

def convert(time):
    tmp = time.split(":")

    if "p.m." in time:
        tmp[0] = int(tmp[0]) + 12
        tmp[1] = tmp[1].replace(" p.m.", "")
    elif "a.m." in time:
        tmp[1] = tmp[1].replace(" a.m.", "")

    return float(int(tmp[0]) + (int(tmp[1])/60))


if __name__ == "__main__":
    main()