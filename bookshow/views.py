from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def bookshow(request):
    queryset = models.Bookshows.objects.all()
    return render(request,"bookshow.html",{"shows":queryset})


def book_show_detail(request,id):
    object = get_object_or_404(models.Bookshows,id=id)
    return render(request,"book_detail.html",{"show":object})
