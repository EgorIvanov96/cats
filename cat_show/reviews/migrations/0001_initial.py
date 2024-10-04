# Generated by Django 5.1.1 on 2024-10-03 15:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Porode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porode_name', models.CharField(help_text='Укажите породу котенка', max_length=150, verbose_name='П орода котенка')),
            ],
            options={
                'verbose_name': 'Порода',
                'verbose_name_plural': 'порода',
            },
        ),
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(help_text='Укажите имя котенка', max_length=150, verbose_name='Имя котенка')),
                ('color_cat', models.CharField(help_text='Укажите цвет котенка', max_length=150, verbose_name='Цвет котенка')),
                ('years', models.PositiveSmallIntegerField(help_text='Укажите возраст(полных месяцев)', verbose_name='Возраст(полных месяцев)')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Хозяин котенка')),
                ('porode_cats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.porode', verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Котенок',
                'verbose_name_plural': 'котенки',
            },
        ),
    ]
