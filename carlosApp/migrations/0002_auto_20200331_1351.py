# Generated by Django 3.0.4 on 2020-03-31 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlosApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airline',
            old_name='airline_act',
            new_name='airline_actif',
        ),
        migrations.AlterField(
            model_name='airline',
            name='airline_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='airport',
            name='airport_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='plane',
            name='plane_name',
            field=models.CharField(max_length=150),
        ),
    ]
