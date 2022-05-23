from django.db import models

# Create your models here.

class Bookshows(models.Model):
    GENRE_CHOICE = (
        ("Fantazy","Fantazy"),
        ("Detective", "Detective"),
        ("Humor", "Humor"),
        ("Roman", "Roman"),
        ("Adveture", "Adveture"),
        ("Science_fiction","Science_fiction")
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to="")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,choices=GENRE_CHOICE)
    tom = models.PositiveIntegerField()


    def __str__(self):
        return self.title