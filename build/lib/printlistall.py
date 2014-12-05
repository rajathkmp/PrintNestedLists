__author__ = 'RK'

"""this file gives function printtab() and printnotab() which prints everything that is present in the list be it nested lists """


def printtab(the_list, level):
    for x in the_list:
        if isinstance(x, list):
            printtab(x, level=level + 1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(x)


def printnotab(the_list):
    for x in the_list:
        if isinstance(x,list):
            printnotab(x)
        else:
            print(x)


print("you have successfully imported printlistall")