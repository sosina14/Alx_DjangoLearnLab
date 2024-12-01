from django.urls import path, include
from .views import  AuthorList, AuthorDetail
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'), # List and create book
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'), # Retrive, Update, Delete book.
    
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Get a specific book
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]

