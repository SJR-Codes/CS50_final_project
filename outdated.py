"""
* CS50P Problem Set 3
* Outdated
* by Samu Reinikainen 24.07.2022
"""

def main():
    #print("What date is it (\"(m/d/y)\")? ", end="")
    udate = get_input("What date is it (\"(m/d/y)\")? ")

    #slist.sort()

    print(udate)

def get_input(prompt):
    x = []
    while True:
        udate = convert_date(input(prompt))
        if udate != False:
            return udate

def convert_date(udate):
    if udate.count("/") == 2:
        return conv_num_date(udate)
    elif udate.count(",") == 1:
        return conv_mon_date(udate)
    else:
        return False

def conv_num_date(udate):
    parts = udate.split("/")
    #print(parts)

    try:
        day = int(parts[1])
        mon = int(parts[0])
        year = int(parts[2])
    except ValueError:
        return False

    if day > 31 or day < 1 or mon > 12 or mon < 1:
        return False

    return str(day).zfill(2) + "-" + str(mon).zfill(2) + "-" + str(year)


def conv_mon_date(udate):
    months = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    parts = udate.split(",")
    year = parts[1].strip()
    parts = parts[0].split(" ")
    try:
        mon = parts[0].strip().lower().title()
        day = parts[1].strip()
    except IndexError:
        return False

    if mon not in months:
        return False

    mon = str(months.index(mon)+1)

    tdate = mon + "/" + day + "/" + year

    return conv_num_date(tdate)

main()