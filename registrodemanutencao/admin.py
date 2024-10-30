from django.contrib import admin
from django.utils.html import format_html
from .models import registrodemanutencao  # Importa o modelo registrodemanutencao.

# Classe para personalizar a exibição do modelo registrodemanutencao no admin.
class RegistroDeManutencaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_produto', 'motivo', 'faturamento',
                    'entregue_por_retirado_por', 'numero_equipamento', 'tratativa', 'imagem_display', 'quantidade',
                    'setor')
    search_fields = ('nome',)  # Permite a busca pelo campo 'nome'.

    # Método para exibir a imagem no admin. (Aqui você pode adicionar lógica para exibir uma miniatura)
    def imagem_display(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.imagem.url)
        return "Sem imagem"

    imagem_display.short_description = "Imagem"  # Define o nome da coluna no admin

# Registra o modelo registrodemanutencao com a classe RegistroDeManutencaoAdmin personalizada.
admin.site.register(registrodemanutencao, RegistroDeManutencaoAdmin)