from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    level = models.IntegerField()
    exp = models.IntegerField()
    consecutive_acess = models.IntegerField(default=1)
    learned_lc = models.ManyToManyField('klass.Lc', related_name='learned_user')
    learned_kw = models.ManyToManyField('klass.kw', related_name='learned_user')


class TestResult(models.Model):
    user = article = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    test_at = models.DateField(auto_now=True)


class AccessDate(models.Model):
    user = article = models.ForeignKey(User, on_delete=models.CASCADE)
    access_at = models.DateField(auto_now_add=True)
