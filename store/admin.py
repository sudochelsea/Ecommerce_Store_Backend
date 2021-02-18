from django.contrib import admin

# Register your models here.
from .models import User
from .models import Product
from .models import Category

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)