from django.contrib import admin

# Register your models here.
from .models.user_profile_model import UserProfile
from .models.product_model import Product
from .models.category_model import Category

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Category)