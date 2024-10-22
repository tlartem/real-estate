# Generated by Django 5.1.2 on 2024-10-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('realty', '0006_remove_building_flats_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='settlement_before',
        ),
        migrations.AddField(
            model_name='building',
            name='settlement_before',
            field=models.DateField(default='2024-12-12', verbose_name='Срок сдачи'),
        ),
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.CharField(
                default='Не указан', max_length=255, verbose_name='Адрес'
            ),
        ),
        migrations.AddField(
            model_name='project',
            name='metro',
            field=models.CharField(
                default='Не указан', max_length=100, verbose_name='Метро'
            ),
        ),
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(
                default='Не указан', max_length=255, verbose_name='Адрес'
            ),
        ),
    ]