from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('book-list', views.BookList.as_view(), name='BookList'),
    path('add-book', views.AddBook.as_view(), name='AddBook'),
    path('details', views.details.as_view(), name='Details'),
]

'''
    path('', views.index.as_view(), name='index'),
    path('book-list', views.BookList, name='BookList'),
    path('add-book', views.AddBook, name='AddBook'),
    path('test', views.test, name='Test'),
    path('details', views.details, name='Details'),
    '''