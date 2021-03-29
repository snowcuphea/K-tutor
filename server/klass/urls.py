from django.urls import path
from . import views

app_name = 'klass'

urlpatterns = [
    path('updateDB', views.updateDB),
    path('cs/list', views.CsViewSet.as_view()),
    path('<str:type>/<str:title>/list', views.LcListViewSet.as_view()),
    path('lc/<int:LcId>', views.LcViewSet.as_view()),
]
