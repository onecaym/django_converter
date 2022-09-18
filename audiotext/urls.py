from django.urls import path, include
from . import views

app_name = 'audiotext'
urlpatterns = [
    path('create_audio/', views.create_audio, name='create_audio'),
]
