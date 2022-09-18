from django.urls import path, include
from . import views

app_name = 'pdf2word_conv'
urlpatterns = [
    path('', views.index, name='index'),
    path('pdf_converter/', views.pdf_converter, name='pdf_converter'),
]
