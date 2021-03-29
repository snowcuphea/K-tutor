from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    level = models.IntegerField(default=1)
    exp = models.IntegerField(default=0)
    consecutive_access = models.IntegerField(default=1)
    learned_lc = models.ManyToManyField('klass.Lc', related_name='learned_user')
    learned_kw = models.ManyToManyField('klass.kw', related_name='learned_user')

    # USERNAME_FIELD = 'user_id'
    # REQUIRED_FIELDS = ['email']


# class AccessDate(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     access_at = models.DateField(auto_now_add=True)
#
# class Acheivement(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     image_on = models.TextField()
#     image_off = models.TextField()
#     achieved = models.ManyToManyField(User, related_name='achieved')
