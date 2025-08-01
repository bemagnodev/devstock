# Generated by Django 5.0.1 on 2025-02-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_generalsuppliesstock_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionsstock',
            name='current_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade Atual'),
        ),
        migrations.AlterField(
            model_name='actionsstock',
            name='minimum_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quant. Mín'),
        ),
        migrations.AlterField(
            model_name='endomarketingstock',
            name='current_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade Atual'),
        ),
        migrations.AlterField(
            model_name='endomarketingstock',
            name='minimum_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quant. Mín'),
        ),
        migrations.AlterField(
            model_name='generalsuppliesstock',
            name='current_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quantidade Atual'),
        ),
        migrations.AlterField(
            model_name='generalsuppliesstock',
            name='minimum_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Quant. Mín'),
        ),
    ]
