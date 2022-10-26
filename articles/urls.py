from django.urls import path, include
from articles import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]