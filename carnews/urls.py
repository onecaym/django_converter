from django.urls import path, include
from . import views

app_name = 'carnews'
urlpatterns = [
    path('news/', views.news, name='news'),
]
