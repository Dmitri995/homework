from django.db import models

class Head_model(models.Model):
    model = models.CharField(max_length=50, unique=True, verbose_name='название наушников')
    manufacturer = models.CharField(max_length=50, unique=True, verbose_name='производитель наушников')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        db_table = 'headphones'
        verbose_name = 'модель'
        verbose_name_plural = 'модели'

    def __str__(self):
        return f'{self.model}'
