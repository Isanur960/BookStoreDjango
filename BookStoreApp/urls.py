from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book-list', views.BookList, name='BookList'),
    path('add-book', views.AddBook, name='AddBook'),
path('test', views.test, name='Test'),
]