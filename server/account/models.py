from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class TestResult(models.Model):
    user = article = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    test_at = models.DateField(auto_now=True)

class AccessDate(models.Model):
    user = article = models.ForeignKey(User, on_delete=models.CASCADE)
    access_at = models.DateField(auto_now_add=True)

class StudiedCpct:
    pass

class StudiedKw:
    pass