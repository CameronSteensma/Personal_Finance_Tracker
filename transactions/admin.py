from django.contrib import admin

# Register your models here.
from .models import Category, Transactions

admin.site.register(Category)
admin.site.register(Transactions)