from django.contrib import admin
from django.contrib.admin.decorators import register
from . models import Pizza, Size
# Register your models here.\


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('topping1', 'topping2', 'size', 'date_created')


# admin.site.register(PizzaAdmin)
admin.site.register(Size)
