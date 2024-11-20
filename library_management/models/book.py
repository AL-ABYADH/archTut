from django.db import models
from .author import Author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    copies_available = models.IntegerField()
