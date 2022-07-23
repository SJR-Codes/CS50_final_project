"""
* CS50P Problem Set 2
* Camel Case
* by Samu Reinikainen 23.07.2022
"""

def main():
    varname = input("Enter variable name: ")

    print(snakify(varname))


def snakify(vname):
    #convert string from camel case to snake case

    ret = ""
    for x in vname:
        #TODO: check that we are not in 1. char and just lower that without underscore
        if x.isupper():
            ret += "_" + x.lower()
        else:
            ret += x

    return ret

main()