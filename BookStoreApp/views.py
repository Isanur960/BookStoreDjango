from django.shortcuts import render
from django.http import HttpResponse
from BookStoreApp.models import  BookDB
from django.contrib import messages
from django.views import View

class index(View):
    def get(self, request):
        return render(request,'index.html')

class BookList(View):
    books = BookDB.objects.all()
    l = []
    lang_list = []
    for book in books:
        lang_list.append(book.lang)
        #print(book.name)
    lang_list_d = list(dict.fromkeys(lang_list))

    genre_list = []
    for book in books:
        genre_list.append(book.genre)
    genre_list_d = list(dict.fromkeys(genre_list))


    def post(self, request):
        genre = request.POST.getlist('genre-s')
        lang = request.POST.getlist('lang-s')
        main0_l = []
        main1_l = []
        if genre != None and len(genre) != 0:
            for key in self.books:
                for g in genre:
                    if key.genre.upper() == g.upper():
                        main0_l.append(key)
                    else:
                        pass
        else:
            main0_l = self.books
        if lang != None and len(lang) != 0:
            for key in main0_l:
                for l in lang:
                    if key.lang.upper() == l.upper():
                        main1_l.append(key)
                    else:
                        pass
        else:
            main1_l = main0_l
        return render(request,'book-list.html', {'books': main1_l, 'langs':self.lang_list_d, 'genres':self.genre_list_d})

    def get(self, request):
        main1_l = self.books
        return render(request,'book-list.html', {'books': main1_l, 'langs':self.lang_list_d, 'genres':self.genre_list_d})


class AddBook(BookList):
    def post(self, request):
        name = request.POST.get('name')
        author = request.POST.get('author')
        genre_s = request.POST.get('genre-s')
        lang_s = request.POST.get('lang-s')
        genre_t = request.POST.get('genre')
        lang_t = request.POST.get('lang')
        if genre_s == 'New':
            genre_f = genre_t
        else:
            genre_f = genre_s

        if lang_s == 'New':
            lang_f = lang_t
        else:
            lang_f = lang_s
        
        books = BookDB.objects.all()

        for book in books:
            check_val = 0
            if book.name.upper() == name.upper():
                check_val += 1
            if book.lang.upper() == lang_f.upper():
                check_val += 1
            if book.genre.upper() == genre_f.upper():
                check_val += 1
            if book.author.upper() == author.upper():
                check_val += 1
            if check_val == 4:
                break
        print(check_val)
        if check_val == 4 :
            messages.add_message(request, messages.ERROR, 'Book already in the database')
        else:
            bookdb =  BookDB(name = name, author = author, genre = genre_f.upper(), lang = lang_f.upper())
            bookdb.save()
            messages.add_message(request, messages.INFO, 'Book Added Successfully ')
        return render(request,'add-book.html',{'langs':self.lang_list_d, 'genres':self.genre_list_d})

    def get(self, request):
        return render(request,'add-book.html',{'langs':self.lang_list_d, 'genres':self.genre_list_d})

class details(View):
    def get(self, request):
        id = request.GET.get('id')
        book_details = BookDB.objects.get(id = id)
        print(book_details.name)
        return render(request, 'details.html',{'book':book_details})
