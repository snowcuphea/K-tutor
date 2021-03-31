from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('signup', views.SignupViewSet.as_view({"post": "post"})),
    path('modify_delete', views.UserViewSet.as_view({"put": "put", "delete": "delete"})),
    path('api/token', obtain_jwt_token),
    path('login', views.LoginViewSet.as_view({"get": "get"})),
    path('get_exp', views.GetexpViewSet.as_view({"post": "post"})),
    path('achievements', views.AchievementViewSet.as_view({"get": "get"}))
]
