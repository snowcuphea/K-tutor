from django.contrib.auth import get_user_model
from django.db import models

class Acheivement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 1. 이미지 파일을 blob 형태로 넣을지
    # 2. ImageField, FileField를 이용해서 넣을지 고민
    image_on = models.BinaryField()
    image_off = models.BinaryField()
    acquired_achievement = models.ManyToManyField(get_user_model(), related_name='achieved')
    #user.achieved.add(obj)
