# Generated by Django 4.0.4 on 2022-05-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0005_druk_cena_papier_cena_rozmiartorby_cena_uchwyt_cena'),
    ]

    operations = [
        migrations.AddField(
            model_name='torba',
            name='cenaTorby',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
