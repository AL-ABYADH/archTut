from library_management.repos.author_repo import AuthorRepo

class AuthorService:
    @classmethod
    def list_authors(cls):
        return AuthorRepo.get_all_authors()

    @classmethod
    def retrieve_author(cls, author_id):
        return AuthorRepo.get_author_by_id(author_id)

    @classmethod
    def create_author(cls, data):
        return AuthorRepo.create_author(data)
