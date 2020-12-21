# 5-6 stages of life: Write an if-elf0else chain that determines a person's stage of life.

age = 80
if age < 2:
    print("You are a baby")
elif age <= 2 and age < 4:
    print("You are a toddler")
elif 4 <= age < 13:
    print("You are a kid")
elif 13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 65:
    print("You are an adult")
else:
    print("You are an elder")
