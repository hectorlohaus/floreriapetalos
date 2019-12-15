from django.contrib import admin
from .models import Flor,Ticket

# Register your models here.

class FlorAdmin(admin.ModelAdmin):
    list_display=('nombre','valor','descripcion','estado','stock')
    searchfields=['nombre','estado']

admin.site.register(Flor,FlorAdmin)
admin.site.register(Ticket)
