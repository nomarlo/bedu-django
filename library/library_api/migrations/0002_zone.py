# Generated by Django 3.2.8 on 2021-11-05 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('latitud', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
            ],
        ),
    ]
