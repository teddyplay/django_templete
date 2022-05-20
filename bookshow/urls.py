
from django.urls import path
from . import views

app_name = "shows_url"
urlpatterns = [
            path('bookshow/',views.bookshow,name="bookshow_all_url"),
            path('bookshow/<int:id>/',views.book_show_detail,name="book_detail_url"),
            path('add_book/',views.add_book_user,name="book_add")
        ]

