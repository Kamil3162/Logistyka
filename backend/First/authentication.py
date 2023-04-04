from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    model = get_user_model()

    def authenticate(self, request,username=None, password=None, **kwargs):

        print("auth started", username, password)
        try:
            user = self.model.objects.get(email_address=username)
            print('esa')
            print(user.password, password)
            if check_password(password, user.password):
                print('correct password')
                return user
            else:
                print("incorrect password")
        except self.model.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
