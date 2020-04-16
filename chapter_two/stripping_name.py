# Isaac Jaramillo 03/23/2020 strips the white/extra space in a variable (first from left,
# then from right, then both)


name = "             \n\tAlireza Firouzja         "
print(name)

print(name.lstrip())

print(name.rstrip())

print(name.strip())
