# Generated by Django 4.2.1 on 2023-06-10 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0006_delete_softwares'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='Buy_Date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
