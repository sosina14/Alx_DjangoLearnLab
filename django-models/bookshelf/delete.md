from bookshelf.models import Book
deleted_book = Book.objects.filter(publication_year=1949)
deleted_book.delete()
-> The above code is used to delete an object with atribute of publication_year 1949.
