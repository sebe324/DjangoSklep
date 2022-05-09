from django.contrib import admin

# Register your models here.
from .models import Papier,Druk,Uchwyt,RozmiarTorby,Torba
admin.site.register(Papier)
admin.site.register(Druk)
admin.site.register(Uchwyt)
admin.site.register(RozmiarTorby)
admin.site.register(Torba)
