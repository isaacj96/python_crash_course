# Ask user to enter text and then displays what they entered

""" message = input("Tell me something, and I will repeat it back to you: ")
print(message) """

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)