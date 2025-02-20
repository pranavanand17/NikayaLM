from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout, authenticate
from .forms import CustomUserCreationForm,CustomLoginForm
from django.contrib import messages
from .models import Book,BorrowedBook
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    book=Book.objects.all()
    return render(request,"book.html", {"book": book})

@login_required
def borrow_book(request,book_id):
    book=get_object_or_404(Book,pk=book_id)

    if BorrowedBook.objects.filter(user=request.user,book=book).exists():
        return redirect("books")

    if book.quantity>0:
        BorrowedBook.objects.create(user=request.user,book=book)
        book.quantity-=1
        book.save()

    return redirect("books")

@login_required
def booksborrowed(request):
    book=BorrowedBook.objects.filter(user=request.user)
    return render(request,"return.html",{"book": book})

@login_required
def fookenreturn(request,book_id):
    borrowed_book=get_object_or_404(BorrowedBook,user=request.user,book_id=book_id)
    book=borrowed_book.book

    borrowed_book.delete()
    book.quantity+=1
    book.save()

    return redirect("return")


def frickinlogin(request):
    if request.method=='POST':
        form=CustomLoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form=CustomLoginForm()

    return render(request,"login.html", {"form": form})

def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request, "Signup successful! Welcome, "+user.username)
            return redirect("home")
        else:
            messages.error(request, "Signup failed. Please check the form.")
    else:
        form=CustomUserCreationForm()
    return render(request,"register.html",{"form":form})

def homepage(request):
    return render(request,'homepage.html')

def signsuccess(request):
    return render(request,'/home/pranavanand/NikayaLM/Nikaya/app/templates/signsuccess.html')

def profile(request):
    return render(request,'/home/pranavanand/NikayaLM/Nikaya/app/templates/profile.html')
