import re

from django.db import models

from django.core.validators import (RegexValidator,
                                    MinValueValidator,
                                    MaxValueValidator,
                                    ValidationError)

def registration_num_validator(reg_num):
    if re.match(r'([A-Z]{2,3})([0-9]{4,5})', reg_num):
        return ValidationError("Register num is not proper")
'''
class Truck(models.Model):
    brand = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=40, blank=False)
    power = models.IntegerField(blank=False,
                                validators=[MinValueValidator(300), MaxValueValidator(999)])
    registration_number = models.CharField(max_length=8,
                                           blank=False,
                                           validators=registration_num_validator)
    driven_length = models.IntegerField(blank=False)
    production_year = models.DateField()
    equipment = models.ForeignKey(TruckEquipment,
                                  on_delete=models.CASCADE,
                                  blank=False)
    def __str__(self):
        return self.brand


class TruckEquipment(models.Model):
    pass
'''

class SemiTrailer(models.Model):
    brand = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=40, blank=False)
    production_year = models.DateField()
    registration_number = models.CharField(max_length=8,
                                           blank=False,
                                           validators=[registration_num_validator], unique=True)
    '''equipment = models.ForeignKey(SemiTrailerEquipment,
                                  on_delete=models.CASCADE,
                                  blank=False)'''



'''
class SemiTrailerEquipment(models.Model):
    pass

class VehicleReceivment(models.Model):
    truck = models.ForeignKey(Truck,
                              on_delete=models.CASCADE,
                              blank=Truck)

    semi_trailer = models.ForeignKey(SemiTrailer,
                                     on_delete=models.CASCADE,
                                     blank=False)
    data_created = models.DateField(auto_created=True)
    data_ended = models.DateField()

'''

