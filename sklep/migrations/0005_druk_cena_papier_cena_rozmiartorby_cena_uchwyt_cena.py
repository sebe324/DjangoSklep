# Generated by Django 4.0.4 on 2022-05-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0004_alter_druk_kolorycmyk_torba'),
    ]

    operations = [
        migrations.AddField(
            model_name='druk',
            name='cena',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='papier',
            name='cena',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rozmiartorby',
            name='cena',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uchwyt',
            name='cena',
            field=models.IntegerField(default=29),
            preserve_default=False,
        ),
    ]
