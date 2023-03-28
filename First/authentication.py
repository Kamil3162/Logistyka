from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request,email_address, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email_address=email_address)
        except user.DoesNotExist:
            return None

        if check_password(password, user.password):
            return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None