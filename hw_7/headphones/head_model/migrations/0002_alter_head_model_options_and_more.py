# Generated by Django 4.0 on 2023-12-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='head_model',
            options={'verbose_name': 'модель', 'verbose_name_plural': 'модели'},
        ),
        migrations.AlterField(
            model_name='head_model',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='head_model',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterModelTable(
            name='head_model',
            table='headphones',
        ),
    ]