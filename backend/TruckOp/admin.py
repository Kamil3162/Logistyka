from django.contrib import admin
from .models import (SemiTrailer,
                    Truck,
                    TruckEquipment,
                    SemiTrailerEquipment,
                    VehicleReceivment)

@admin.register(SemiTrailer)
class SemiTrailerAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'registration_number', 'semi_note')

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'registration_number', 'avaiable')

@admin.register(TruckEquipment)
class TrackEquipment(admin.ModelAdmin):
    list_display = ('truck', 'avaiable', 'complete_status')

@admin.register(SemiTrailerEquipment)
class SemiTrailerEquipmentAdmin(admin.ModelAdmin):
    list_display = ('semi_trailer', 'corners','aluminium_stick')

@admin.register(VehicleReceivment)
class VehicleReceivmentAdmin(admin.ModelAdmin):
    list_display = ['truck','semi_trailer', 'data_created', 'user']