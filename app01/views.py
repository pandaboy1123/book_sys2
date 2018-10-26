from django.shortcuts import render, HttpResponse, redirect
from .models import Publish, Author, Book, AuthorDeatil
# Create your views here.


def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")
        book_obj = Book.objects.create(title=title, price=price, publishDate=pub_date, publish_id=publish_id)
        book_obj.authors.add(*authors_id_list)
        return redirect("/index/")
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, "addbook.html", locals())


def index(request):
    book_list = Book.objects.all()
    pub_list = Publish.objects.all()
    au_list = Author.objects.all()
    au_name = []
    pu_name = []
    for n in au_list:
        au_name.append(n.name)
    for n in pub_list:
        pu_name.append(n.name)
    if request.method == "POST":
        name = request.POST.get('name')
        # print(name)
        # 根据作者拿到所有的书本
        if name in au_name:
            author_obj = Author.objects.get(name=name)
            book_list_1 = author_obj.book_set.all()
        # 根据出版社拿到所有的书本
        elif name in pu_name:
            pub_obj = Publish.objects.get(name=name)
            book_list_1 = pub_obj.book_set.all()
    return render(request, "index.html", locals())
    # return HttpResponse("OK")


def change_book(request, edit_id):
    edit_book_obj = Book.objects.filter(pk=edit_id).first()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.getlist("authors_id_list")
        Book.objects.filter(pk=edit_id).update(title=title, price=price, publishDate=pub_date,
                                                    publish_id=publish_id)
        edit_book_obj.authors.set(authors_id_list)
        return redirect("/index/")
    return render(request, "changebook.html", locals())


def delete_book(request, del_id):
    Book.objects.filter(pk=del_id).delete()
    return redirect("/index/")


