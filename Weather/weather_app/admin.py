from django.contrib import admin
from .models import WeatherData

class MyAdmin(admin.ModelAdmin):
    list_display = ('city','temperature','humidity','condition','wind_speed','recorded_at')
admin.site.register(WeatherData,MyAdmin)
