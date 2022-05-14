from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book


def get_all_books(request):
    books_qs = Book.objects.all()
    return  render(request=request, template_name='book.html', context={'all_books':books_qs})