from django.urls import path
from . import views

app_name = 'class'

urlpatterns = [
    path('updateDB/', views.updateDB),
    path('<str:type>/list', views.CsViewSet.as_view({"get": "list"})),
    path('<str:type>/<str:title>/list', views.LcListViewSet.as_view({"get": "list"})),
    path('<int:LcId>', views.LcViewSet.as_view({"get": "get"})),
]
