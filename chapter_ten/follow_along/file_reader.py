file_name = 'py_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
# print(line.rstrip())
# for line in file_object:
#     print(line.rstrip())
# contents = file_object.read()
# print(contents.rstrip())
