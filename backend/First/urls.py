from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usrcreate', views.CreateUserAPI.as_view(), name='registration'),
    path('logout', views.LogoutUserAPI.as_view(), name='logout'),
    path('login', views.LoginUserAPI.as_view(), name='login')
]