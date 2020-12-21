# starting with list we created in guest_list.py and change the set of invitations because one guest can't make it
guest_list = ['Lionel Messi', 'Einstein', 'Elon Musk']
print(guest_list)

print(f"Hi, {guest_list[0].title()}, would you like to come to dinner with me?")
print(f"Hi, {guest_list[1].title()}, would you like to come to dinner with me?")
print(f"Hi, {guest_list[2].title()}, would you like to come to dinner with me?")

# Changes to original program begins here

print(f"Oh no! Looks like {guest_list[0]} won't be able to make it, better look for someone else to invite.")

guest_list[0] = 'Carl Sagan'
print(f"Hi, {guest_list[0].title()}, would you like to come to dinner with me?")
print(
    f"Hi, {guest_list[1].title()}, I had to send out another set of invitations, but would you still like to come to dinner with me?")
print(
    f"Hi, {guest_list[2].title()}, I had to send out another set of invitations, but would you still like to come to dinner with me?")
