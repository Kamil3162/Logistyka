from django.contrib import admin
from .models import SemiTrailer
# Register your models here.
@admin.register(SemiTrailer)
class SemiTrailerAdmin(admin.ModelAdmin):
    list_display = '__all__'