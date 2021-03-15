from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(to=get_user_model(), related_name="user_profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s profile"