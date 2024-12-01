from datetime import date
from .models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    # The BookSerializer serializes all fields of the Book model.
    class Meta:
        model = Book
        fields = '__all__'
        
    # Custom validation to ensure the publication year is not in the future.
    def validate_publication_year(self, publication_year):
        if publication_year > date.today().year:
            raise serializers.ValidationError("Publication year can not be in the future.")
        return publication_year
    
class AuthorSerializer(serializers.ModelSerializer):
    # The AuthorSerializer serializes the name of the Author and includes a nested BookSerializer. 
    # # This dynamically serializes related books for each author.
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']
    