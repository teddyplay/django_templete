
from django.urls import path
from . import views

app_name = "shows_url"
urlpatterns = [
            path('bookshow/',views.bookshow,name="bookshow_all_url"),
            path('bookshow/latest/',views.books_latest,name="latest"),
            path('bookshow/Fantazy/',views.books_Fantazy,name="Fantazy"),
            path('bookshow/Detective/',views.books_Detective,name="Detective"),
            path('bookshow/Humor/',views.books_Humor,name="Humor"),
            path('bookshow/Roman/',views.books_Roman,name="Roman"),
            path('bookshow/Adveture/',views.books_Adveture,name="Adveture"),
            path('bookshow/Science_fiction/',views.books_Science_fiction,name="Science_fiction"),
            path('bookshow/<int:id>/',views.book_show_detail,name="book_detail_url"),
            path('bookshow/<int:id>/update/',views.book_update,name="book_update"),
            path('bookshow/<int:id>/delete/',views.book_delete,name="book_delete"),
            path('add_book/',views.add_book_user,name="book_add")
        ]

