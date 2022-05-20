from django.db import models


class Book(models.Model): # TODO называть модели во множествнном числе
    """модель для книг"""
# TODO прочитать что такое ORM и зачем он нужен
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)




