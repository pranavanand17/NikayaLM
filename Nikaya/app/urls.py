from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static 

urlpatterns=[
    path('register/',views.register,name='register'),
    path('',views.homepage,name='home'),
    path('login/',views.frickinlogin,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signsuccess/',views.signsuccess,name='signsuccess'),
    path('profile/',views.profile,name='profile'),
    path("books/",views.book_list,name="books"),
    path("borrow/<int:book_id>/",views.borrow_book,name="borrow_book"),
    path("return/",views.booksborrowed,name="return"),
    path("return/<int:book_id>/",views.fookenreturn,name="return_book"),
]



