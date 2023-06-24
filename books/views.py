from django.shortcuts import render

from django.http import HttpResponse
from .models import Book


# Create your views here.
def index(request):
    books_list = Book.objects.order_by("-read_date").all()
    context = {"books_list": books_list}
    return render(request, "index.html", context)
