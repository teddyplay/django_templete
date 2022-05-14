from django.contrib import admin
from django.urls import path
from book.views import get_all_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_all_books),
]