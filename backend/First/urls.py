from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usercreate', views.CreateUserAPI.as_view(), name='registration')
]