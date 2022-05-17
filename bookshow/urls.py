
from django.urls import path
from . import views

urlpatterns = [
            path('bookshow/',views.bookshow,name="bookshow_all_url"),
            path('bookshow/<int:id>/',views.book_show_detail,name="book_detail_url")
        ]

