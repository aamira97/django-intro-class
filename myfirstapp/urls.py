from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='myfirstapp-home'),
    path('user/', views.user, name='myfirstapp-user'),
    path('class5/', views.class5, name='myfirstapp-user')
    # path('about/', views.about, name='myfirstapp-about')
    # path('', views.home, name='myfirstapp-home')
]
