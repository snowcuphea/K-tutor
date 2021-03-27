from django.urls import path
from . import views

urlpatterns = [
    path('modify_delete/', views.account_modify_delete),
]