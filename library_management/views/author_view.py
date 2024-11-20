from rest_framework import viewsets
from rest_framework.response import Response
from library_management.serializers.author_serializer import AuthorSerializer
from library_management.services.author_service import AuthorService

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = AuthorService.list_authors()
    serializer_class = AuthorSerializer
