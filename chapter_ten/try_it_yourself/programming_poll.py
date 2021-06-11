file_name = 'programming_poll.txt'

with open(file_name, 'a') as file_object:
    name = ''
    while name != 'q' or name == 'quit':
        name = input("Why do you like programming?\n")
        if name == 'q' or name == 'quit':
            break
        else:
            file_object.write(name + "\n")
