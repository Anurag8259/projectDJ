# Generated by Django 4.2.1 on 2023-06-09 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_softwares'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hardware',
            old_name='Asset_ID',
            new_name='asset_id',
        ),
        migrations.RenameField(
            model_name='hardware',
            old_name='Hardware_Name',
            new_name='hardware_name',
        ),
        migrations.RenameField(
            model_name='hardware',
            old_name='Location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='hardware',
            old_name='Price',
            new_name='price',
        ),
    ]
