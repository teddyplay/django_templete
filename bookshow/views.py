from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect,reverse
from . import models,forms
# Create your views here.

def bookshow(request):
    queryset = models.Bookshows.objects.all()
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
