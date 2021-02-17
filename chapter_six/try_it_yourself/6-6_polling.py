# 6-6 Polling. Use the code in favorite_languages.py

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Creating a list of people who should take a poll

ask_people = ['bill', 'Jean', 'John', 'edward', 'sarah']

# Printing a statement for each scenario based on whether a person has answered the poll already or not
for people in ask_people:
    if people in favorite_languages.keys():
        print("Thank you for responding!")
    elif people not in favorite_languages.keys():
        print("Please take the poll!")