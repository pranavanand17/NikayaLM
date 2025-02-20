from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta
from django.utils import timezone

class CustomUser(AbstractUser):
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,unique=True,null=True)
    profile_photo=models.ImageField(upload_to="profile_photos/",blank=True,null=True,default='profile_photos/default.jpg')

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username","phone_number"]

    def __str__(self):
        return self.username

class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    genre=models.CharField(max_length=100,blank=True,null=True)
    cover_photo=models.ImageField(upload_to="cover_photos/",blank=True,null=True,default='profile_photos/default.jpg')
    publication_date=models.DateField(blank=True,null=True)
    quantity=models.IntegerField(default=1)
    isbn=models.CharField(max_length=13,unique=True)
    added_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class BorrowedBook(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="borrowed_books")
    book=models.ForeignKey(Book, on_delete=models.CASCADE,related_name="borrowers")
    borrow_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(blank=True,null=True)
    fine=models.DecimalField(max_digits=6,decimal_places=2,default=0.00)

    def save(self, *args, **kwargs):
        if not self.return_date:
            if not self.borrow_date:
                self.borrow_date=timezone.now()
            self.return_date=self.borrow_date+timedelta(days=7)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

