from library_management.models.author import Author
from library_management.repos.book_repo import BookRepo
from library_management.exceptions.book_has_no_author_exception import BookHasNoAuthorException

class AuthorRepo:
    @classmethod
    def get_all_authors(cls):
        return Author.objects.all()

    @classmethod
    def get_author_by_id(cls, author_id):
        return Author.objects.get(id=author_id)

    @classmethod
    def create_author(cls, data):
        return Author.objects.create(**data)

    @classmethod
    def get_book_author(cls, id):
        book = BookRepo.get_book_by_id(id)
        author = book.author
        if author is None:
            raise BookHasNoAuthorException
        return author

