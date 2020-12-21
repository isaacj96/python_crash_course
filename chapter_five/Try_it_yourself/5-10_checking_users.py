current_users = ['John', 'stevie', 'Tropicana', 'true Clear', 'Beebee']
new_users = ['Mike', 'Hawk', 'Bumble', 'Tropicana', 'Stevie']

lowerList = [item.lower() for item in current_users]
print(lowerList)

for user in new_users:
    user.lower()
    if user in lowerList:
        print(f"{user.lower()}, please enter a new username")
    else:
        print(f"{user}, username is avaliable")
