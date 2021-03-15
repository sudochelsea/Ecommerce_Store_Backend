from django.db import models
from django.contrib.auth import get_user_model


class Order(models.Model):
    user = models.ForeignKey(to=get_user_model(), related_name='orders', on_delete=models.CASCADE )
    quantity = models.IntegerField(default=1)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.quantity
