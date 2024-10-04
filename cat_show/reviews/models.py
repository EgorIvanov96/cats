from django.db import models

from users.models import User


class Porode(models.Model):
    """Класс пород"""

    porode_name = models.CharField(
        max_length=150,
        verbose_name='Порода котенка',
        help_text='Укажите породу котенка'
    )

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'порода'

    def __str__(self):
        return self.porode_name


class Cats(models.Model):
    """Класс котенков"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Хозяин котенка'
    )
    porode_cats = models.ForeignKey(
        Porode,
        on_delete=models.CASCADE,
        verbose_name='Порода'
    )
    cat_name = models.CharField(
        max_length=150,
        verbose_name='Имя котенка',
        help_text='Укажите имя котенка',
        unique=True
    )
    color_cat = models.CharField(
        max_length=150,
        verbose_name='Цвет котенка',
        help_text='Укажите цвет котенка'
    )
    years = models.PositiveSmallIntegerField(
        verbose_name='Возраст(полных месяцев)',
        help_text='Укажите возраст(полных месяцев)'
    )

    class Meta:
        verbose_name = 'Котята'
        verbose_name_plural = 'котята'

    def __str__(self):
        return self.cat_name
