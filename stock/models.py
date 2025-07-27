from django.db import models
from .email_utils import send_email
from django.utils.timezone import localtime

class BaseStockItem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome do Produto")
    current_quantity = models.PositiveIntegerField(default=0,verbose_name="Quantidade Atual")
    specification = models.TextField(blank=True, verbose_name="Especificação")
    minimum_quantity = models.PositiveIntegerField(default=0 ,verbose_name="Quant. Mín")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Unitário (R$)", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")
    last_update_display = models.CharField(max_length=20, blank=True, verbose_name="Última Modificação")
    image = models.ImageField(
        upload_to='stock_images/',
        blank=True,
        null=True,
        help_text="O tamanho recomendado para a imagem é quadrado (ex: 500x500 px).",
        verbose_name="Foto do Item")
    LOCALIZACOES_CHOICES = [
        ('SP', 'São Paulo'),
        ('FOR', 'Fortaleza'),
        ('EUS', 'Eusébio'),
    ]

    location = models.CharField(
        choices=LOCALIZACOES_CHOICES,
        max_length=10,
        verbose_name="Localização",
        default='FOR'  
        )

    class Meta:
        abstract = True 
    def is_below_minimum(self):
        """Verifica se a quantidade atual está abaixo ou igual ao mínimo."""

        return self.current_quantity <= self.minimum_quantity

    def save(self, *args, **kwargs):
        """Atualiza o campo de exibição da última modificação"""
        super().save(*args, **kwargs) 
        
        self.last_update_display = localtime(self.updated_at).strftime('%d/%m/%y às %H:%M')

        if self.is_below_minimum():
            subject = f"⚠️ Alerta: Estoque baixo - {self.name}"
            body = (
                f"O item '{self.name}' atingiu ou está abaixo da quantidade mínima no estoque.\n\n"
                f"Especificação: {self.specification}\n"
                f"Quantidade Atual: {self.current_quantity}\n"
                f"Quantidade Mínima: {self.minimum_quantity}\n\n"
                f"Por favor, reponha este item o mais rápido possível."
            )
            send_email(
                to_email="albuquerque@teclat.com.br",

                subject=subject,
                body=body,
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class EndomarketingStock(BaseStockItem):
    class Meta:
        verbose_name = "Estoque de Endomarketing"
        verbose_name_plural = "Estoque de Endomarketing"


class GeneralSuppliesStock(BaseStockItem):
    class Meta:
        verbose_name = "Suprimentos Gerais"
        verbose_name_plural = "Suprimentos Gerais"

class ActionsStock(BaseStockItem):
    class Meta:
        verbose_name = "Estoque de Ações"
        verbose_name_plural = "Estoque de Ações"

    
