from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('', views.UserViewSet.as_view({"post": "post", "put": "put", "delete": "delete"})),
    path('api/token', obtain_jwt_token),
    path('login', views.LoginViewSet.as_view({"get": "get"}))
]
