from django.contrib import admin
from .models import Category, Customer, Product, Order


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# Registering the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('email',)
    ordering = ('first_name', 'last_name')


# Registering the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    ordering = ('name', 'category')


# Registering the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'status', 'date_ordered', 'phone', 'address')
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name', 'phone')
    list_filter = ('status', 'date_ordered')
    ordering = ('date_ordered', 'status')
