from django.contrib import admin
from .models import CarMake
from .models import CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'type', 'year']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'manufacturer']
    inlines = [CarModelInline]


# Registering models with their respective admins
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
