# Objective is to print out the "ordinal numbers" or print the position in a list. eg. 1st, 2nd, 3rd...has to have that th or st

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in list:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
