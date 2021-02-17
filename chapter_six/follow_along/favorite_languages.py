""" favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# for n, l in favorite_languages.items():
#     print(f"\nName: {n.title()}")
#     print(f"Favorite Language: {l.title()}")
#     print(f"{n.title()}\'s favorite language is {l.title()}.")

# for n in favorite_languages.keys():
#     print(n.title())

friends = ['phil', 'sarah', ]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):  # use set to skip duplicates
    print(language.title())
 """

favorite_lanuages = {
     'jen': ['python', 'ruby'],
     'sarah': ['c'],
     'edward': ['ruby', 'go'],
     'phil': ['python', 'haskell'],
 }

for name, lanuages in favorite_lanuages.items():
    if len(lanuages) == 1:
        print(f"{name.title()}'s favorite language is: {lanuages}")
    else: 
        print(f"{name.title()}'s favorite languages are:")
        for lanuage in lanuages:
            print(f"\t{lanuage.title()}")