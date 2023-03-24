import re

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.core.exceptions import ValidationError
from django.core.validators import (RegexValidator,
                                    MinValueValidator,
                                    MaxValueValidator)

class CustomUserManager(BaseUserManager):
    def create_user(self):
        pass

    def create_superuser(self):
        pass

def zip_code_valid(zip_code:str):
    if re.match(r'([0-9]{2})+-([0-9]{3})', zip_code):
        return True
    return ValidationError("Zip code isnt properly")

def mobile_address_valid(mobile_phone:str):
    if re.match(r'^([1-9]{1})+[0-9]{8}', mobile_phone):
        return True
    return ValidationError("Mobile phone is not properly")

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('CEO', 'CO'),
        ('DIRECTOR', 'DR')
        ('DRIVER','EM')
    )
    name = models.CharField(max_length=40, blank=False)
    surname = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    region = models.CharField(max_length=60, blank=False)
    zip_code = models.CharField(max_length=6,
                                validators=[zip_code_valid])
    email_address = models.EmailField(max_length=80, blank=False)
    mobile_phone = models.CharField(max_length=9, validators=mobile_address_valid)
    role = models.CharField(max_length=8, choices=ROLES, default='DRIVER')

    is_active = True
    is_superuser = False
    is_staff = False

    def __str__(self):
        return self.id

