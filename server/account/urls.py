from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('modify_delete/', views.account_modify_delete),
]