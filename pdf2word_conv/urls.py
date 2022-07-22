from django.urls import path, include
from . import views

app_name = 'pdf2word_conv'
urlpatterns = [
    path('', views.index, name='index'),
    path('conv_to_word/', views.conv_to_word, name='conv_to_word'),
    path('success/', views.success, name='success'),
]
