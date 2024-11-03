from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields displayed in the admin list view
    search_fields = ('title', 'author')  # Adds search functionality by title and author
    list_filter = ('publication_year',)  # Adds filter by publication year
