username = []
if username:
    for user in username:
        if user == 'admin':
            print(f"Greeting's {user}! Would you like to see a status report?")
        print(f"Welcome back {user}! Thank you for logging in again.")
else:
    print("We need to find some users!")
