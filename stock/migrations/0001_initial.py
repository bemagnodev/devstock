# Generated by Django 5.0.1 on 2025-01-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionsStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do Produto')),
                ('current_quantity', models.PositiveIntegerField(verbose_name='Quantidade Atual')),
                ('specification', models.TextField(blank=True, verbose_name='Especificação')),
                ('minimum_quantity', models.PositiveIntegerField(verbose_name='Quantidade Mínima de Estoque')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
            ],
            options={
                'verbose_name': 'Estoque de Ações',
                'verbose_name_plural': 'Estoque de Ações',
            },
        ),
        migrations.CreateModel(
            name='CleaningProductsStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do Produto')),
                ('current_quantity', models.PositiveIntegerField(verbose_name='Quantidade Atual')),
                ('specification', models.TextField(blank=True, verbose_name='Especificação')),
                ('minimum_quantity', models.PositiveIntegerField(verbose_name='Quantidade Mínima de Estoque')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
            ],
            options={
                'verbose_name': 'Estoque de Produtos de Limpeza',
                'verbose_name_plural': 'Estoque de Produtos de Limpeza',
            },
        ),
        migrations.CreateModel(
            name='EndomarketingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome do Produto')),
                ('current_quantity', models.PositiveIntegerField(verbose_name='Quantidade Atual')),
                ('specification', models.TextField(blank=True, verbose_name='Especificação')),
                ('minimum_quantity', models.PositiveIntegerField(verbose_name='Quantidade Mínima de Estoque')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Atualização')),
            ],
            options={
                'verbose_name': 'Estoque de Endomarketing',
                'verbose_name_plural': 'Estoque de Endomarketing',
            },
        ),
    ]
