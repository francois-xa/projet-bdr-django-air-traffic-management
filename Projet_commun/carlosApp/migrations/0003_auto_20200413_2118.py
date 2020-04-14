# Generated by Django 3.0.3 on 2020-04-13 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carlosApp', '0002_auto_20200331_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airport',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='city',
            name='country_id',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='airline_id',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='airport_id_dest',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='airport_id_source',
        ),
        migrations.RemoveField(
            model_name='routes',
            name='plane_id',
        ),
        migrations.DeleteModel(
            name='Airline',
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Plane',
        ),
        migrations.DeleteModel(
            name='Routes',
        ),
    ]