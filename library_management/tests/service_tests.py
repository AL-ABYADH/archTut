from unittest.mock import patch
from django.test import TestCase
from library_management.services.author_service import AuthorService
from library_management.services.book_service import BookService
from library_management.models.author import Author
from library_management.models.book import Book

class AuthorServiceTest(TestCase):
    @patch('library_management.repos.author_repo.AuthorRepo.get_all_authors')
    def test_list_authors(self, mock_get_all_authors):
        mock_get_all_authors.return_value = [Author(name="Test Author", bio="Test Bio")]
        authors = AuthorService.list_authors()
        self.assertEqual(len(authors), 1)
        self.assertEqual(authors[0].name, "Test Author")

    @patch('library_management.repos.author_repo.AuthorRepo.get_author_by_id')
    def test_retrieve_author(self, mock_get_author_by_id):
        mock_get_author_by_id.return_value = Author(name="Test Author", bio="Test Bio")
        author = AuthorService.retrieve_author(1)
        self.assertEqual(author.name, "Test Author")

    @patch('library_management.repos.author_repo.AuthorRepo.create_author')
    def test_create_author(self, mock_create_author):
        mock_create_author.return_value = Author(name="New Author", bio="New Bio")
        new_author_data = {"name": "New Author", "bio": "New Bio"}
        author = AuthorService.create_author(new_author_data)
        self.assertEqual(author.name, new_author_data["name"])

class BookServiceTest(TestCase):
    @patch('library_management.repos.book_repo.BookRepo.get_all_books')
    def test_list_books(self, mock_get_all_books):
        mock_get_all_books.return_value = [Book(title="Test Book", author_id=1, isbn="1234567890123", published_date="2023-01-01", copies_available=5)]
        books = BookService.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

    @patch('library_management.repos.book_repo.BookRepo.get_book_by_id')
    def test_retrieve_book(self, mock_get_book_by_id):
        mock_get_book_by_id.return_value = Book(title="Test Book", author_id=1, isbn="1234567890123", published_date="2023-01-01", copies_available=5)
        book = BookService.retrieve_book(1)
        self.assertEqual(book.title, "Test Book")

    @patch('library_management.repos.book_repo.BookRepo.create_book')
    def test_create_book(self, mock_create_book):
        mock_create_book.return_value = Book(title="New Book", author_id=1, isbn="9876543210987", published_date="2024-01-01", copies_available=10)
        new_book_data = {"title": "New Book", "author": 1, "isbn": "9876543210987", "published_date": "2024-01-01", "copies_available": 10}
        book = BookService.create_book(new_book_data)
        self.assertEqual(book.title, new_book_data["title"])
