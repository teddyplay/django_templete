from django.shortcuts import render
from . import models
# Create your views here.

def bookshow(request):
    queryset = models.Bookshows.objects.all()
    return render(request,"bookshow.html",{"shows":queryset})
