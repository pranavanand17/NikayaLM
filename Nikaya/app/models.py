from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin= models.BooleanField(default=False)

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='book_images'/)
    quantity=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    def borrow(self):
        """Reduce the quantity by 1 when borrowed."""
        if self.quantity>0:
            self.quantity-=1;
            self.save()
        else:
            raise ValueError("No copies left to borrow!")

    def return_book(self):
        """Increase the quantity by 1 when returned."""
        self.quantity+=1
        self.save()

