my_file = 'learning_python.txt'

with open(my_file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'C++').rstrip())
