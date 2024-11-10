all_book = Book.objects.get(title='1984')
-> The above command is used to retrieve all the book instance created.

for book in all_book:
    print(f'{book.title}, {book.author}, {book.publication_year}')

-> The for loop is used to iterate all the book instance created and print them one by one separately.