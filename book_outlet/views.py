from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-rating')
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": books.count(),
        "avg_rating": books.aggregate(Avg("rating"))
    })

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return render_book(request, book)

def book_detail_slug(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render_book(request, book)

def render_book(request, book):
    return render(request, 'book_outlet/book_detail.html', {
        "title" : book.title,
        "author" : book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
    })