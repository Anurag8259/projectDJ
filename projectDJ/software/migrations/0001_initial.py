# Generated by Django 4.2.1 on 2023-06-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_name', models.CharField(max_length=50)),
                ('buy_date', models.DateField()),
            ],
        ),
    ]
