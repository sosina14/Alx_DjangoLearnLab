# Retrieve all books
books = Book.objects.all()
print(books)  # This will show a queryset of all Book objects

# Retrieve a single book by title
book_1984 = Book.objects.get(title="1984")
print(book_1984)
