from library_management.repos.book_repo import BookRepo
from library_management.repos.author_repo import AuthorRepo
from library_management.exceptions.book_has_no_author_exception import BookHasNoAuthorException

class BookService:
    def __init__(cls, book_repo = BookRepo):
        cls.book_repo = book_repo


    @classmethod
    def list_books(cls):
        # return BookRepo.get_all_books()
        return cls.book_repo.get_all_books()

    @classmethod
    def retrieve_book(cls, book_id = 1):
        return BookRepo.get_book_by_id(book_id)

    @classmethod
    def create_book(cls, data):
        return BookRepo.create_book(data)

    @classmethod
    def update_book(cls, book_id, data):
        return BookRepo.update_book(book_id, data)

    @classmethod
    def get_author(cls, book_id, data):
        try:
            res = AuthorRepo.get_book_author()
        except BookHasNoAuthorException:
            return "NOT FOUND"
        
        return res