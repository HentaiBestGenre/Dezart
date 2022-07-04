from django.urls import path

from . import views

app_name = 'The_Site'
urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.send_info, name='send_form'),
    path('culc', views.calculator, name='calculator'),
]