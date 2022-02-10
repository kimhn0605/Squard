from django.urls import path
from . import views

# http://logalhost/home/
app_name = 'home'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('mypage/', views.mypage, name='mypage'),
    path('dice/', views.dice, name='dice'),
]
