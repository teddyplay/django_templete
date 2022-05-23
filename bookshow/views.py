from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect,reverse
from . import models,forms
from datetime import datetime,timedelta

start_date = datetime.today() - timedelta(days=5)

def bookshow(request):
    queryset = models.Bookshows.objects.order_by("id")
    return render(request,"bookshow.html",{"shows":queryset})


def book_show_detail(request,id):
    object = get_object_or_404(models.Bookshows,id=id)
    return render(request,"book_detail.html",{"show":object})




def add_book_user(request):
    method = request.method
    if method == "POST":
        form = forms.Form_for_bookshow(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("TVShow Created successfully")
            return redirect(reverse("shows_url:bookshow_all_url"))
    else:
        form = forms.Form_for_bookshow()
    return render(request, "add_shows.html", {"form": form})



def book_update(request,id):
    book_object = get_object_or_404(models.Bookshows,id = id)
    if request.method == "POST":
        form = forms.Form_for_bookshow(instance=book_object,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("shows_url:bookshow_all_url"))
    else:
        form = forms.Form_for_bookshow(instance=book_object)
    return render(request,"book_update.html",{"form":form,
                                                "object":book_object})


def book_delete(request, id):
    book_object = get_object_or_404(models.Bookshows, id=id)
    book_object.delete()
    return redirect(reverse("shows_url:bookshow_all_url"))



def books_latest(request):
    queryset = models.Bookshows.objects.filter(created_date__gt=start_date).order_by("-id")
    return render(request, "bookshow.html", {"shows": queryset})


def books_Fantazy(request):
    main = models.Bookshows.objects.filter(genre="Fantazy").order_by("-id")
    return render(request,"bookshow.html",{"shows":main})

def books_Detective(request):
    queryset = models.Bookshows.objects.filter(genre="Detective").order_by("-id")
    return render(request,"bookshow.html",{"show":queryset})

def books_Humor(request):
    queryset = models.Bookshows.objects.filter(genre="Humor").order_by("-id")
    return render(request,"bookshow.html",{"show":queryset})

def books_Roman(request):
    queryset = models.Bookshows.objects.filter(genre="Roman").order_by("-id")
    return render(request,"bookshow.html",{"shows":queryset})

def books_Adveture(request):
    queryset = models.Bookshows.objects.filter(genre="Adveture").order_by("-id")
    return render(request,"bookshow.html",{"shows":queryset})


def books_Science_fiction(request):
    queryset = models.Bookshows.objects.filter(genre="Science_fiction").order_by("-id")
    return render(request,"bookshow.html",{"shows":queryset})