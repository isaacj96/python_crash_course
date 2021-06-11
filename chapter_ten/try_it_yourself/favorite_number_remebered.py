import json


def get_stored_number():
    """Get user name if available"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(number, f)
            print(f"We'll remember you when you come back, {number}!")
    else:
        return number


def get_new_number():
    """Prompt for a new username"""
    number = input("What is your favorite number? ")
    filename = "favorite_number.json"
    with open(filename, 'w') as f:
        json.dump(number, f)
        return number


def print_favorite_number():
    """Greet user by name."""
    number = get_stored_number()
    if number:
        print(f"Favorite number is, {number}!")
    else:
        username = get_new_number()
        print(f"Your favorite number, {number}, has now been stored")


print_favorite_number()
