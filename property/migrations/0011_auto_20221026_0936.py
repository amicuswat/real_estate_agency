# Generated by Django 3.2 on 2022-10-26 06:36

from django.db import migrations

import phonenumbers


def fill_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            flat.owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber,
                                                       'RU')
        except TypeError:
            continue
        flat.save()


def move_backwards(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = ''
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(fill_phones)
        # migrations.RunPython(fill_phones, move_backwards)
    ]
