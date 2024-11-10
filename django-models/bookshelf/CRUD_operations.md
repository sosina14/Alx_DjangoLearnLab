from bookshelf.models import Book
new_book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
new_book.save()

all_book = Book.objects.all()
for book in all_book:
    print(f'{book.title}, {book.author}, {book.publication_year}')

updated_book = Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four')

deleted_book = Book.objects.filter(publication_year=1949).delete()