from django.contrib import admin
from library_management.models.author import Author
from library_management.models.book import Book

admin.site.register(Author)
admin.site.register(Book)