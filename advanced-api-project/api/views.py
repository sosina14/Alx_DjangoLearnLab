from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework import filters
# from rest_framework import  generics
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from .permission import IsAuthorOrReadOnly
from django_filters import rest_framework

# Create your views here.

# View to create a new author with permission checks and custom validations.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    
    def create_author(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    # View to update an author with custom validations and permission checks.    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def update_author(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        author = self.get_object()
        serializer = self.get_serializer(author, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookListView(generics.ListAPIView):
    # view to list all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Allow read-only access
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year'] # Enable filtering
    search_fields = ['title', 'author__name'] # This will allow to filter books by their title and author name.
    ordering_fields = ['title', 'publication_year'] #Allow ordering by those mentioned fields
    ordering = ['title']  # Default ordering
    
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned books to a given author,
    #     by filtering against an `author_id` query parameter in the URL.
    #     """
    #     queryset = Book.objects.all()
    #     # Access query_params from the request
    #     author_id = self.request.query_params.get('author_id', None)
    #     if author_id is not None:
    #         queryset = queryset.filter(author__id=author_id)
    #     return queryset
    
class BookDetailView(generics.RetrieveAPIView):
    # view to retrive a single book by Id
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Read-only access
    
class BookCreateView(generics.CreateAPIView):
    # view to create a new book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # Restrict to authenticated users
    
    def perform_create(self, serializer):
        # Custome method to perform the creattion of a book instance
        serializer.save()
        
class BookUpdateView(generics.UpdateAPIView):
    # view to update an existing book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
    
    def perform_update(self, serializer):
        # custom method to perform the update of the book instance
        serializer.save()
        # custom update 
    def update_book(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data, partial=partial)
        serializer.is_valid(raise_excepption=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookDeleteView(generics.DestroyAPIView):
    # view to delete a book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # restrict to authenticated users.
    
    
