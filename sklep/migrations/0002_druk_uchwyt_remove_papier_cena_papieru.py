# Generated by Django 4.0.4 on 2022-04-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Druk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koloryCMYK', models.IntegerField()),
                ('pelnyZadruk', models.BooleanField()),
                ('blyszczacyLaminat', models.BooleanField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='uchwyt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('szerokosc', models.IntegerField()),
                ('wciecieWTorbie', models.BooleanField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='papier',
            name='cena_papieru',
        ),
    ]
