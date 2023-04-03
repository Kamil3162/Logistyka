from rest_framework import routers
from django.urls import path
from .views import (UsersDisplay,
                    TruckDisplay,
                    SamiTruckDisplay)
urlpatterns = [
    path('trucks', TruckDisplay.as_view(), name='trucks')
]
router = routers.SimpleRouter()
router.register(r'users', UsersDisplay)
router.register(r'samitrucks', SamiTruckDisplay)

urlpatterns += router.urls


