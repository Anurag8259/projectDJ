# Generated by Django 4.2.1 on 2023-06-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0003_software_software'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='software',
            name='Software',
        ),
        migrations.AlterField(
            model_name='software',
            name='validity',
            field=models.CharField(choices=[('yearly', 'Yearly'), ('lifetime', 'Lifetime'), ('monthly', 'Monthly')], default='Lifetime', max_length=50),
        ),
    ]
