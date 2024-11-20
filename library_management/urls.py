from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.author_view import AuthorViewSet
from .views.book_view import BookViewSet

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="authors")
router.register("books", BookViewSet, basename="books")

urlpatterns = [
    path("", include(router.urls)),
]
