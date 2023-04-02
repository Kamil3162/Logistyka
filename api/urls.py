from rest_framework import routers
from django.urls import path
from .views import (UsersDisplay,
                    TruckDisplay)
urlpatterns = [
    path('trucks', TruckDisplay.as_view(), 'trucks')
]
router = routers.SimpleRouter()
router.register(r'users', UsersDisplay)

urlpatterns += router.urls


