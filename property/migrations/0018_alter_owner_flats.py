# Generated by Django 3.2 on 2022-10-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20221031_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности:'),
        ),
    ]
