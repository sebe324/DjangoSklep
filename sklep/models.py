from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator
class Papier(models.Model):
    class Meta:
        managed=True
    class Rozmiar(models.TextChoices):
        A0="A0", _('841x1189')
        A1="A1", _('594x841')
        B1="B1", _('707x1000')
        B2="B2", _('500x707')
    rozmiar=models.CharField(
        max_length=2,
        choices=Rozmiar.choices
    )
    class Gramatura(models.IntegerChoices):
        ciezki=200
        sredni=150
        lekki=100
    gramatura=models.IntegerField(choices=Gramatura.choices)
    powlekany=models.BooleanField()
class Druk(models.Model):
    class Meta:
        managed=True
    koloryCMYK=IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    pelnyZadruk=models.BooleanField()
    blyszczacyLaminat=models.BooleanField()
class Uchwyt(models.Model):
    class Meta:
        managed=True
    szerokosc=models.IntegerField()
    wciecieWTorbie=models.BooleanField()
class RozmiarTorby(models.Model):
    class Meta:
        managed=True
    class Szerokosc(models.IntegerChoices):
        mala=30
        srednia=60
        dluga=90
    class Dlugosc(models.IntegerChoices):
        cienka=20
        gruba=40
    class Wysokosc(models.IntegerChoices):
        krotka=20
        srednia=40
        wysoka=60
    szerokosc=models.IntegerField(choices=Szerokosc.choices)
    dlugosc=models.IntegerField(choices=Dlugosc.choices)
    wysokosc=models.IntegerField(choices=Szerokosc.choices)
class Torba(models.Model):
    papier=models.ForeignKey('Papier', on_delete=models.CASCADE)
    druk=models.ForeignKey('Druk', on_delete=models.CASCADE)
    uchwyt=models.ForeignKey('Uchwyt', on_delete=models.CASCADE)
    rozmiarTorby=models.ForeignKey('RozmiarTorby', on_delete=models.CASCADE)
    











