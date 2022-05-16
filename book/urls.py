from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('book/', views.Book,name="shows_all_url"),
        ]

