from unittest.mock import patch
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from library_management.models.author import Author
from library_management.models.book import Book

class AuthorViewSetTest(APITestCase):
    @patch('library_management.services.author_service.AuthorService.list_authors')
    def test_list_authors(self, mock_list_authors):
        mock_list_authors.return_value = [Author(name="Test Author", bio="Test Bio")]
        url = reverse('author-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Author")

    @patch('library_management.services.author_service.AuthorService.create_author')
    def test_create_author(self, mock_create_author):
        mock_create_author.return_value = Author(name="New Author", bio="New Bio")
        new_author_data = {"name": "New Author", "bio": "New Bio"}
        url = reverse('author-list')
        response = self.client.post(url, new_author_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], new_author_data["name"])

class BookViewSetTest(APITestCase):
    @patch('library_management.services.book_service.BookService.list_books')
    def test_list_books(self, mock_list_books):
        mock_list_books.return_value = [Book(title="Test Book", author_id=1, isbn="1234567890123", published_date="2023-01-01", copies_available=5)]
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    @patch('library_management.services.book_service.BookService.create_book')
    def test_create_book(self, mock_create_book):
        mock_create_book.return_value = Book(title="New Book", author_id=1, isbn="9876543210987", published_date="2024-01-01", copies_available=10)
        new_book_data = {"title": "New Book", "author": 1, "isbn": "9876543210987", "published_date": "2024-01-01", "copies_available": 10}
        url = reverse('book-list')
        response = self.client.post(url, new_book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], new_book_data["title"])
