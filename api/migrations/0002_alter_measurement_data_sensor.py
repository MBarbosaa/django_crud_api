# Generated by Django 4.0 on 2021-12-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='data_sensor',
            field=models.FloatField(),
        ),
    ]