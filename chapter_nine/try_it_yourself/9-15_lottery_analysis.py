from random import choice

my_list = [54, 42, 90, 27, 32, 0, 1, 50, 100, 32, 'b', 'c', 'd', 'e', 'r']

i = 0
x = 4
my_ticket = ['d', 42, 90, 100]


def get_winning_ticket(aList):
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled = choice(aList)
        winning_ticket.append(pulled)
    return winning_ticket


def compare_tickets(alist, comparinglist):
    for element in alist:
        if element not in comparinglist:
            return False
    return True


won = False
while not won:
    winning_ticket = get_winning_ticket(my_list)
    won = compare_tickets(winning_ticket, my_ticket)
    i += 1

print(i)
