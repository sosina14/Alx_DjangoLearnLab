from django.contrib import admin
from .models import Book
# from .models import Product

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("title", "author")

# Register your models here.
admin.site.register(Book, BookAdmin)
# admin.site.register(Product)



