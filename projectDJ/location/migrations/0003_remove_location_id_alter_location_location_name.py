# Generated by Django 4.2.1 on 2023-06-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_location_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='id',
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
