from django.contrib import admin
from .models import EndomarketingStock, GeneralSuppliesStock, ActionsStock
from django.contrib import messages
from django.utils.html import format_html

# Personalização do cabeçalho e título
admin.site.site_header = "Painel de Controle de Estoque"
admin.site.site_title = "DevStock"
admin.site.index_title = "Bem-vindo ao DevStock!"


# Filtro de Localização 
class LocationFilter(admin.SimpleListFilter):
    title = 'Localização'
    parameter_name = 'location'

    def lookups(self, request, model_admin):
        return [
            ('SP', 'São Paulo'),
            ('FOR', 'Fortaleza'),
            ('EUS', 'Eusébio'),
        ]

    def queryset(self, request, queryset):
        if self.value():
             return queryset.filter(location=self.value())
        return queryset

# Classe Base para os modelos de estoque
class BaseStockAdmin(admin.ModelAdmin):
    list_display = ( 'image_preview','name', 'specification', 'current_quantity', 'minimum_quantity', 'unit_price', 'location',  'last_update_display', 'is_below_minimum_display')
    list_display_links = ('name', 'image_preview',)
    list_filter = (LocationFilter,)
    search_fields = ('name', 'specification')
    ordering = ('name',)
    list_editable = ('current_quantity', 'unit_price') 
    readonly_fields = ('created_at', 'last_update_display', 'image_preview')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'specification',  'location', 'image_preview', 'image')
        }),
        ('Controle de Estoque', {
            'fields': ('current_quantity', 'minimum_quantity', 'unit_price',)
        }),
        ('Datas', {
            'fields': ('created_at', 'last_update_display',)
        }),
    )

    def is_below_minimum_display(self, obj):
        """Exibe status do estoque com destaque em vermelho quando abaixo do mínimo."""
        if obj.is_below_minimum():
            return format_html('<span style="color: red; font-weight: bold;">⚠️ Estoque Baixo</span>')
        return format_html('<span style="color: green; font-weight: bold;">✅ OK</span>')
    is_below_minimum_display.short_description = "Status do Estoque"

    def image_preview(self, obj):
        """Exibe uma prévia da imagem no Django Admin."""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.image.url)
        return "Sem imagem"
    image_preview.short_description = "Imagem"

    def save_model(self, request, obj, form, change):
        if obj.is_below_minimum():
            messages.warning(request, f"⚠️ Quantidade de {obj.name} abaixo do mínimo. Por favor, reponha o estoque.")
        super().save_model(request, obj, form, change)

@admin.register(EndomarketingStock)
class EndomarketingStockAdmin(BaseStockAdmin):
    pass

@admin.register(GeneralSuppliesStock)
class CleaningProductsStockAdmin(BaseStockAdmin):
    pass

# @admin.register(ActionsStock)
# class ActionsStockAdmin(BaseStockAdmin):
#     pass
