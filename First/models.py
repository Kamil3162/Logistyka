import re
import django.core.validators
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.core.exceptions import ValidationError
from django.core.validators import (RegexValidator,
                                    MinValueValidator,
                                    MaxValueValidator)

class CustomUserManager(BaseUserManager):
    def create_user(self, name, surname, city, region, zip_code,
                    email_address, mobile_phone,password=None, **extra_fields):
        if not name:
            raise ValueError("Please enter you name")
        if not surname:
            raise ValueError("Please enter you name")
        if not city:
            raise ValueError("Please enter you city")
        if not region:
            raise ValueError("Please enter you name")
        if not zip_code:
            raise ValueError("Please enter zip code:")


        user = self.model(
            name=name,
            surname=surname,
            city=city,
            region=region,
            zip_code=zip_code,
            email_address=self.normalize_email(email_address),
            mobile_phone=mobile_phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, name, surname, city, region, zip_code,
                    email_address, mobile_phone,password=None, **extra_fields):
        user = self.create_user(
            name=name,
            surname=surname,
            city=city,
            region=region,
            zip_code=zip_code,
            email_address=email_address,
            mobile_phone=mobile_phone,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

def email_validator(email_add):
    if re.match(r'([A-Za-z0-9]{25}[.-_]*[A-Za-z0-9]{10}@([A-Za-z]{10})+(\.[A-Za-z]{2,}))', email_add):
        return ValidationError("Email is not propertly")

def zip_code_valid(zip_code):
    if re.match(r'^([0-9]{2})+-([0-9]{3})', zip_code):
        return ValidationError("Zip code isnt properly")

def mobile_address_valid(mobile_phone):
    if not re.match(r'^([1-9]{1})+[0-9]{8}', mobile_phone):
        return ValidationError("Mobile phone is not properly")

class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''
    ROLES = (
        ('CEO', 'CO'),
        ('DIRECTOR', 'DR')
        ('DRIVER','EM')
    )'''
    #role = models.CharField(max_length=8, choices=ROLES, default='DRIVER')
    name = models.CharField(max_length=40, blank=False)
    surname = models.CharField(max_length=40, blank=False)
    city = models.CharField(max_length=40, blank=False)
    region = models.CharField(max_length=60, blank=False)
    zip_code = models.CharField(max_length=6,
                                validators=[zip_code_valid], blank=False)
    email_address = models.EmailField(max_length=80, blank=False,
                                      unique=True, validators=[email_validator])
    mobile_phone = models.CharField(max_length=9, validators=[mobile_address_valid], unique=True)
    password = models.CharField(max_length=180, blank=False)

    is_active = models.BooleanField(default=True,blank=False)
    is_superuser = models.BooleanField(default=False,blank=False)
    is_staff = models.BooleanField(default=False,blank=False)
    is_admin = models.BooleanField(default=False, blank=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email_address"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email_address



