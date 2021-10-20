from django.urls import path
from . import views

urlpatterns = [
    path('', views.human, name='homework2-page')
]
