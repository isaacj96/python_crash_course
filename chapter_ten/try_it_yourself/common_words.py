books = ['Alice in Wonderland', ]

for book in books:
    with open(book) as f:
        read = f.read()
        content = read.lower().count("the ")
        compare = read.count("the ")
        print(content)
        print(compare)
