# Generated by Django 3.2 on 2022-10-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20221028_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
