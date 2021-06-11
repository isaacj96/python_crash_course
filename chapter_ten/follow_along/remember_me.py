import json


def get_stored_username():
    """Get user name if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        return username


def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name?")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username


def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()
