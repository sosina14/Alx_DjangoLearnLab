> from bookshelf.models import Book 
    -> The above command used to import the Book class from bookshelf app
> new_book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
    -> This command will create the book instance(object)
> new_book.save()
    -> after creating the book object the above command will save the instanmce in to the database.