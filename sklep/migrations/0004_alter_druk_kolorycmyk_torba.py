# Generated by Django 4.0.4 on 2022-05-09 22:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0003_rozmiartorby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='druk',
            name='koloryCMYK',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.CreateModel(
            name='Torba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('druk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.druk')),
                ('papier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.papier')),
                ('rozmiarTorby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.rozmiartorby')),
                ('uchwyt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.uchwyt')),
            ],
        ),
    ]
