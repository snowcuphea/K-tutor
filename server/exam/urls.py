from django.urls import path
from . import views

app_name = 'exam'

urlpatterns = [
    path('report', views.ExamReportViewSet.as_view({"get": "get"})),
    path('', views.ExamViewSet.as_view({"get": "get", "post": "post"}))
]
