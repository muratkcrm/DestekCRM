from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    users = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    telefon = models.CharField(max_length=30)
    dogumTarihi = models.DateField()
