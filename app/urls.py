from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('food/', views.food, name="food"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.search, name="search"),
    path('detail/', views.detail, name="detail"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('update_item/', views.updateItem, name="update_item"),
    path('category/', views.category, name="category"),

]