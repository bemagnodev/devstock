# Generated by Django 5.0.1 on 2025-02-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_actionsstock_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionsstock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stock_images/', verbose_name='Foto do Item'),
        ),
        migrations.AddField(
            model_name='actionsstock',
            name='last_update_display',
            field=models.CharField(blank=True, max_length=20, verbose_name='Última Modificação'),
        ),
        migrations.AddField(
            model_name='actionsstock',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Unitário'),
        ),
        migrations.AddField(
            model_name='cleaningproductsstock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stock_images/', verbose_name='Foto do Item'),
        ),
        migrations.AddField(
            model_name='cleaningproductsstock',
            name='last_update_display',
            field=models.CharField(blank=True, max_length=20, verbose_name='Última Modificação'),
        ),
        migrations.AddField(
            model_name='cleaningproductsstock',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Unitário'),
        ),
        migrations.AddField(
            model_name='endomarketingstock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stock_images/', verbose_name='Foto do Item'),
        ),
        migrations.AddField(
            model_name='endomarketingstock',
            name='last_update_display',
            field=models.CharField(blank=True, max_length=20, verbose_name='Última Modificação'),
        ),
        migrations.AddField(
            model_name='endomarketingstock',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Unitário'),
        ),
        migrations.AlterField(
            model_name='actionsstock',
            name='minimum_quantity',
            field=models.PositiveIntegerField(verbose_name='Quant. Mín'),
        ),
        migrations.AlterField(
            model_name='cleaningproductsstock',
            name='minimum_quantity',
            field=models.PositiveIntegerField(verbose_name='Quant. Mín'),
        ),
        migrations.AlterField(
            model_name='endomarketingstock',
            name='minimum_quantity',
            field=models.PositiveIntegerField(verbose_name='Quant. Mín'),
        ),
    ]
