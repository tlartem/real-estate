# Generated by Django 5.1.2 on 2024-10-21 06:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                (
                    'description',
                    models.TextField(blank=True, null=True, verbose_name='Описание'),
                ),
                (
                    'price',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name='Цена',
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[('On sale', 'В продаже'), ('Sold', 'Продана')],
                        default='On sale',
                        max_length=7,
                        verbose_name='Статус',
                    ),
                ),
                (
                    'rooms',
                    models.PositiveSmallIntegerField(verbose_name='Кол-во комнат'),
                ),
                (
                    'area',
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name='Площадь',
                    ),
                ),
                (
                    'kitchen_area',
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name='Кухня',
                    ),
                ),
                ('floor', models.PositiveSmallIntegerField(verbose_name='Этаж')),
                ('settlement_before', models.DateField(verbose_name='Заселение после')),
                (
                    'building',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='flats',
                        to='realty.building',
                        verbose_name='Корпус',
                    ),
                ),
                (
                    'project',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='realities',
                        to='realty.project',
                        verbose_name='Проект',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='building',
            name='project',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='buildings',
                to='realty.project',
            ),
        ),
    ]
