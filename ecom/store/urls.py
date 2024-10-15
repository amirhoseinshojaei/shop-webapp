from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pk>', views.product_details, name='product_details'),
    path('category/<str:slug>', views.category_details, name='category_details'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]