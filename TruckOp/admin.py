from django.contrib import admin
from .models import (SemiTrailer,
                    Truck,
                    TruckEquipment,
                    SemiTrailerEquipment)

admin.site.register(SemiTrailer)
admin.site.register(Truck)
admin.site.register(TruckEquipment)
admin.site.register(SemiTrailerEquipment)
