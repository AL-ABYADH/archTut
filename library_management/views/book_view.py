from rest_framework import viewsets
from rest_framework.response import Response
from library_management.serializers.book_serializer import BookSerializer
from library_management.services.book_service import BookService

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        books = BookService.list_books()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = BookService.retrieve_book(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        book = BookService.create_book(data)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=201)

    def update(self, request, pk=None):
        data = request.data
        book = BookService.update_book(pk, data)
        serializer = BookSerializer(book)
        return Response(serializer.data)
