from django.core.signals import request_finished
from django.dispatch import receiver
from .models import User

@receiver(User.checkAchievement)
def updateUserAchivement(sender, user, **kwargs):
    pass