file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
    name = input("Please enter your name.\n")
    file_object.write(name)
