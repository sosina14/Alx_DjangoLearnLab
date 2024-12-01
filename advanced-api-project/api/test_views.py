from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book,Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    # Set up a user for authentication
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        # Create a test author instance
        self.author = Author.objects.create(name='Author 1')  # Create an author instance

        # create a test book instance
        self.book = Book.objects.create(title='Test Book', author=self.author, publication_year=2023)
        
    def test_create_book(self):
        url = reverse('book-create')
        # Create a new author instance for the new book
        new_author = Author.objects.create(name='Author 2')
        data = {
            'title': 'New Book',
            'author': new_author.id,  # Reference to the newly created author
            'publication_year': 2024
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Check that the book count has increased
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')
        
    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # should return the test Book
        self.assertEqual(response.data[0]['title'], self.book.title)
        
    def test_get_single_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        
    def test_update_book(self):
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Book Title'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Update Book Title')
        
    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        
    def test_filter_books_by_year(self):
        url = reverse('book-list') + '?search=Test'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)   # should return the test book
        
    def test_order_books(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_permissions(self):
        self.client.logout()  # logout the user
        url = reverse('book-create')
        data = {'title': 'Unauthenticated Book', 'author': 'Author 3', 'publication_year': 2023}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # should deny access