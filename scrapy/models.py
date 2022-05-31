from django.db import models


class Watchs(models.Model):
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Tehchnodom(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title