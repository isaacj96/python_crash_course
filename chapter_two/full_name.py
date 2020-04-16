#Isaac Jaramillo 03/23/2020
# Declared two variables and combined the first and last name into one variable, 
# from there I declared a message variable that said Hello then the persons name via the full name variable
# that message variable was then printed

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)