from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    product_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name, allow_unicode=True)
        #super allows you to save changes you make to a method in the model class(overiding a method)
        super(Category, self).save(*args, **kwargs)