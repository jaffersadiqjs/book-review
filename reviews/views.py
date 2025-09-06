from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Review

def book_list(request):
    books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    return render(request, 'reviews/book_detail.html', {'book': book, 'reviews': reviews})

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        Review.objects.create(book=book, user=request.user, rating=rating, comment=comment)
        return redirect('book_detail', pk=pk)
    return render(request, 'reviews/add_review.html', {'book': book})
