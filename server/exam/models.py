from django.db import models

from server import settings


class ExamResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

