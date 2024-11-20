from library_management.models.book import Book

class BookRepo:
    @classmethod
    def get_all_books(cls):
        return Book.objects.all()

    @classmethod
    def get_book_by_id(cls, book_id):
        return Book.objects.get(id=book_id)

    @classmethod
    def create_book(cls, data):
        return Book.objects.create(**data)

    @classmethod
    def update_book(cls, book_id, data):
        book = Book.objects.get(id=book_id)
        for key, value in data.items():
            setattr(book, key, value)
        book.save()
        return book
