"""Defines URL patterns for books app"""

from rest_framework.routers import SimpleRouter
from apps.books import views

app_name = "books"
router = SimpleRouter()
router.register("books", views.BooksView)

urlpatterns = router.urls