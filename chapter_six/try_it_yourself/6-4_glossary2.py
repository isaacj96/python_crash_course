python_gloss = {
    'variable': 'Something that holds information',
    'List': 'Collection of items in a particular list',
    'For Loop': "A loop that x amount of times, usually with a iterator",
    'If loop': 'A loop that continues running until the condition is either true or false',
    'Tuple': 'A non-mutable list',
    'Set': 'A mutable list that skips duplicates',
    'Python Standard Library': 'Pre-existing code written to help you such as numpy or pandas.',
    'Print': 'Part of the Python STL, it displays text onto the screen.',
    'Input': 'Stores user input as a string in Python.',
    'Dictionary': 'Store data in key value pairs.'
}
# print(f"Variable: {python_gloss['variable']}\nList: {python_gloss['List']}\nFor Loop: {python_gloss['For Loop']}\
# \nIf Loop: {python_gloss['If loop']}\nTuple: {python_gloss['Tuple']}")

for k, v in python_gloss.items():
    print(f"Keyword: '{k}', definition: '{v}'.")
