from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('book/<book_id>', views.detail, name = 'detail'),
    path('add/',views.add_book,name='add_book'),
    path('update/<book_id>', views.update, name = 'update'),
]