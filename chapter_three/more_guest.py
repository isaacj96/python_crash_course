# starting with list we created in guest_list.py and change the set of invitations because one guest can't make it
guest_list = ['Lionel Messi', 'Einstein', 'Elon Musk']
print(guest_list)

print(f"Hi, {guest_list[0].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[1].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[2].title()}, would you like to come to dinner with me?\n")

# Changes to original program begins here

print(f"Oh no! Looks like {guest_list[0]} won't be able to make it, better look for someone else to invite.\n")

guest_list[0] = 'Carl Sagan'
print(f"Hi, {guest_list[0].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[1].title()}, I had to send out another set of invitations, but would you still like to come "
      f"to dinner with me?\n")
print(f"Hi, {guest_list[2].title()}, I had to send out another set of invitations, but would you still like to come "
      f"to dinner with me?\n")

#3.6 changes begin here
print("We found a bigger table! We will be inviting more guest now!")

guest_list.insert(0, 'James Bond')
guest_list.insert(2, 'Bobby Fischer')
guest_list.append('Magnus Carlsen')

print(f"Hi, {guest_list[0].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[1].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[2].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[3].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[4].title()}, would you like to come to dinner with me?\n")
print(f"Hi, {guest_list[5].title()}, would you like to come to dinner with me?\n")


