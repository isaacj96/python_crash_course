file_name = 'guest_book.txt'

with open(file_name, 'w') as file_object:
    name = ''
    while name != 'q' or name == 'quit':
        name = input("Please enter your name. type 'q' or 'quit' to exit.\n")
        if name == 'q' or name == 'quit':
            break
        else:
            file_object.write(name + "\n")
