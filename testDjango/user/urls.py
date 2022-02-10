from django.urls import path
from . import views

# http://logalhost/user
app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('mypage', views.mypage, name='mypage'),
    path('logout/', views.logout, name='logout'),
]
