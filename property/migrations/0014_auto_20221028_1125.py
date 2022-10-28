# Generated by Django 3.2 on 2022-10-28 08:25

from django.db import migrations


def fill_owners(apps, shema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(name=flat.owner,
                                    phonenumber=flat.owners_phonenumber,
                                    pure_phone=flat.owner_pure_phone)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_owner_flats'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]
