# bookshelf/forms.py

from django import forms
from .models import Book  # Assuming a Book model exists

class ExampleForm(forms.ModelForm):
    """
    An example model form tied to the Book model.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
