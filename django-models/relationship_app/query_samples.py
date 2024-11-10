# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library

def get_books_by_author(author_name):
    try:
        # Retrieve the Author object
        author = Author.objects.get(name=author_name)
        # Query all books by this specific author
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []  # Return an empty list if the author doesn't exist

def get_books_in_library(library_id):
    try:
        # Retrieve the Library object
        library = Library.objects.get(id=library_id)
        # List all books in the library using the ManyToManyField relationship
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []  # Return an empty list if the library doesn't exist

def get_librarian_for_library(library_id):
    try:
        # Retrieve the Library object
        library = Librarian.objects.get(library=library_id)
        # library =  Library.objects.get(name=library_name)
        # library = Library.objects.get(id=library_id)
        # Access the related Librarian using the OneToOneField relationship
        # librarian = library.librarian
        return library
    except Library.DoesNotExist:
        return None  # Return None if the library doesn't exist
