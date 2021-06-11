def count_words(file_name):
    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


filenames = ['cas.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        pass
