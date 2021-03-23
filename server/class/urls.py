from django.urls import path
from . import views

app_name = 'class'

urlpatterns = [
    path('updateDB/', views.updateDB),
]