from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('signup', views.sign_up),
    path('modify_delete', views.account_modify_delete),
    path('api/token', obtain_jwt_token),
    # path('login', views.LoginViewSet.as_view({"get": "login"}))
    path('login', views.login)
]