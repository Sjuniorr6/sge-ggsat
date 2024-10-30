from typing import Any
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from .forms  import EstoqueantenistarForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from registrodemanutencao.models import registrodemanutencao
from requisicao.models import Requisicoes,estoque_antenista
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.conf import settings
from registrodemanutencao.forms import FormulariosUpdateForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
#------------------------------------------------------
class RequisicoesViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "requisicoes.html"
    context_object_name = 'requisicoes'
    paginate_by = 12
    permission_required = "requisicao.view_requisicoes"
    
    def get_queryset(self):
        return Requisicoes.objects.filter(status__in=['Pendente'])
    


from django.http import JsonResponse
from .models import Clientes


def get_cliente_data(request, cliente_id):
    cliente = Clientes.objects.get(id=cliente_id)
    data = {
        'cnpj': cliente.cnpj,
        'inicio_de_contrato': cliente.inicio_de_contrato,
        'vigencia': cliente.vigencia,
        'contrato': cliente.tipo_contrato,
       
    }
    return JsonResponse(data) 
import logging
from django.contrib import messages
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Requisicoes, estoque_antenista
from .forms import RequisicaoForm

logger = logging.getLogger(__name__)
class RequisicaoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Requisicoes
    template_name = 'requisicao_create.html'
    form_class = RequisicaoForm
    success_url = reverse_lazy('requisicoes')
    permission_required = "requisicao.add_requisicoes"

    def get_queryset(self):
        return Requisicoes.objects.all().order_by('id')

    def form_valid(self, form):
        motivo = form.cleaned_data.get('motivo')
        antenista = form.cleaned_data.get('antenista')
        tipo_produto = form.cleaned_data.get('tipo_produto')
        numero_de_equipamentos = form.cleaned_data.get('numero_de_equipamentos')

        logger.info("Formulário válido: %s", form.is_valid())
        logger.info("Dados do formulário: %s", form.cleaned_data)

        if motivo in ['Isca FAST', 'Estoque Antenista'] and antenista and tipo_produto and numero_de_equipamentos:
            try:
                with transaction.atomic():
                    requisicao = form.save(commit=False)
                    quantidade_requisitada = int(numero_de_equipamentos)
                    antenista_estoque, created = estoque_antenista.objects.get_or_create(
                        nome=antenista, 
                        tipo_produto=tipo_produto, 
                        defaults={'quantidade': 0}
                    )
                    
                    if antenista_estoque.quantidade is None:
                        antenista_estoque.quantidade = 0

                    if motivo == 'Isca FAST':
                        if antenista_estoque.quantidade >= quantidade_requisitada:
                            antenista_estoque.quantidade -= quantidade_requisitada
                        else:
                            messages.error(self.request, f"O antenista {antenista} não tem quantidade suficiente no estoque para o produto {tipo_produto}. Quantidade disponível: {antenista_estoque.quantidade}, quantidade requisitada: {quantidade_requisitada}.")
                            return self.form_invalid(form)
                    elif motivo == 'Estoque Antenista':
                        antenista_estoque.quantidade += quantidade_requisitada
                    
                    antenista_estoque.save()
                    requisicao.save()
                    return super().form_valid(form)
            except Exception as e:
                logger.error("Erro ao processar a requisição: %s", e)
                messages.error(self.request, "Ocorreu um erro ao processar a requisição.")
                return self.form_invalid(form)
        else:
            return super().form_valid(form)
    

    
class RequisicaoDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = models.Requisicoes
    template_name = 'requisicao_detail.html'
    permission_required="requisicao.view_requisicoes"


class RequisicaoUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Requisicoes
    form_class = forms.RequisicaoForm
    template_name = 'requisicao_update.html'
    context_object_name = 'requisicao'
    success_url = reverse_lazy('requisicao_list')
    permission_required="requisicao.change_requisicoes"
class Requisicao2UpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Requisicoes
    form_class = forms.RequisicaoForm
    template_name = 'requisicao_update.html'
    context_object_name = 'requisicao'
    success_url = reverse_lazy('requisicao_list')
    permission_required="requisicao.change_requisicoes"

  

class requisicoesdeleteview(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = models.Requisicoes
    template_name = 'requisicao_delete.html'
    success_url = reverse_lazy('acompanhamento_requisicao')
    permission_required="requisicao.delete_requisicoes"
#------------------------------------------------------

#------------------------------------------------------
class configuracaodeleteview(PermissionRequiredMixin,LoginRequiredMixin,DeleteView):
    model = models.Requisicoes
    template_name = 'configuracao_delete.html'
    success_url = reverse_lazy('acompanhamento_requisicao')
    permission_required="requisicao.delete_requisicoes"


class ConfiguracaoListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    template_name = 'configuracao_list.html'
    context_object_name = 'equipamentos'
    permission_required= "requisicao.view_requisicoes"
    
    
    def get_queryset(self):
        
        
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['Aprovado pelo CEO']).exclude(tipo_produto__nome__in=['GS310','GS340','GS390','GS8310 (4G)'])
        manutencao_queryset = registrodemanutencao.objects.filter(status__in=['Aprovado Inteligência', 'Aprovado pela Diretoria', 'Aprovado pelo CEO']).exclude(tipo_produto__nome__in=['GS310','GS340','GS390','GS8310 (4G)'])
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset


class ConfiguracaoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Requisicoes
    form_class = forms.requisicaoFormup
    template_name = 'configuracao_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('ConfiguracaoListView')
    permission_required = "requisicao.change_requisicoes"

class ConfiguracaoUpdateView2(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = registrodemanutencao
    form_class = FormulariosUpdateForm
    template_name = 'configuracao_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('ConfiguracaoListView')
    permission_required = "requisicao.change_requisicoes"
  

 #------------------------------------------------------   


class tecnicoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = 'setor_tecnico.html'
    context_object_name = 'equipamentos'
    permission_required = "requisicao.view_requisicoes"
    
    def get_queryset(self):
        valores_tipo_produto = ['GS310', 'GS340', 'GS390', 'GS8310 (4G)']
        requisicao_queryset = Requisicoes.objects.filter(tipo_produto__nome__in=valores_tipo_produto)
        return requisicao_queryset


class tecnicoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Requisicoes
    form_class = forms.requisicaoFormup
    template_name = 'setor_tecnico_update.html'
    context_object_name = 'equipamento'
    success_url = reverse_lazy('tecnicoListView')
    permission_required = "requisicao.change_requisicoes"


#------------------------------------------------------





from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from .models import Requisicoes

class ceoListViews(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "ceo_list.html"
    context_object_name = 'ceo_list'
    paginate_by = 10
    permission_required = "requisicao.view_requisicoes"

    def get_queryset(self):
        return Requisicoes.objects.filter(status__in=['Pendente', 'Aprovado pela Diretoria'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_pendente'] = Requisicoes.objects.filter(status='Pendente').count()
        context['total_aprovado_ceo'] = Requisicoes.objects.filter(status='Aprovado pelo CEO').count()
        context['total_configurado'] = Requisicoes.objects.filter(status='Configurado').count()
        
        # Verificando requisições que não foram alteradas nas últimas 24 horas, excluindo 'Enviado para o Cliente'
        threshold_time = timezone.now() - timedelta(hours=24)
        context['requisições_sem_alteracao'] = Requisicoes.objects.filter(
            data_alteracao__lt=threshold_time
        ).exclude(status='Enviado para o Cliente')  # Exclui o status 'Enviado para o Cliente'
        
        # Contando requisições sem alteração
        context['count_requisicoes_sem_alteracao'] = context['requisições_sem_alteracao'].count()
        
        return context
  

class ceodetailview(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = Requisicoes
    template_name = 'ceo_detail.html'
    permission_required="requisicao.view_requisicoes"


class CeoEntradaDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    model = registrodemanutencao
    template_name = 'ceo_detalheentrada.html'
    context_object_name = 'manutencoes'
    permission_required="requisicao.view_requisicoes"
#------------------------------------------------------


#------------------------------------------------------


class diretoriaListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    template_name = "diretoria_list.html"
    context_object_name = 'diretoria_list'
    permission_required="requisicao.view_requisicoes"
    
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['', ''])
        manutencao_queryset = registrodemanutencao.objects.filter(status='Manutenção')
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset
#------------------------------------------------------


from django.views.generic import ListView
from formacompanhamento.models import Formacompanhamento  # Substitua 'Financeiro' pelo nome do seu modelo

class FinanceiroListViews(ListView):
    template_name = "financeiro_list.html"  # Substitua pelo nome do seu template
    context_object_name = 'financeiro_list'
    paginate_by = 10

    def get_queryset(self):
        return Formacompanhamento.objects.all()  # Defina o queryset aqui
    









#------------------------------------------------------
class expedicaoListViews(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = Requisicoes
    template_name = "expedicao_list.html"
    context_object_name = 'expedicao_list'
    permission_required="requisicao.view_requisicoes"
    
       
    def get_queryset(self):
        requisicoes_queryset = Requisicoes.objects.filter(status__in=['Configurado'])
        manutencao_queryset = registrodemanutencao.objects.filter(status__in=['Configurado'])
        
        # Combine os querysets
        combined_queryset = list(requisicoes_queryset) + list(manutencao_queryset)
        
        return combined_queryset
#------------------------------------------------------
#------------------------------------------------------
class historicoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = "historico_list.html"
    context_object_name = 'historico_list'
    paginate_by = 12
    permission_required = "requisicao.view_requisicoes"
    
    def get_queryset(self):
        queryset = Requisicoes.objects.all().order_by('-id')
        nome = self.request.GET.get('nome')
        status = self.request.GET.get('status')
        
        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        
        if status:
            queryset = queryset.filter(status__icontains=status)
        
        return queryset

#------------------------------------------------------





#------------------------------------------------------
def aprovar_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Aprovado pela Diretoria'
    registro.save()
    return redirect('#')

def reprovar_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Reprovado pela Diretoria'
    registro.save()
    return redirect('#')
#------------------------------------------------------

def aprovar_FINANCEIRO(request, id):
    registro = get_object_or_404(Formacompanhamento, id=id)
    registro.status = 'PAGO'
    registro.save()
    return redirect('FinanceiroListViews')





#------------------------------------------------------
def reprovar_ceo(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Reprovado pelo CEO'
    registro.save()
    
    return redirect('ceoListViews')


def aprovar_ceo(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Aprovado pelo CEO'
    registro.save()
    subject = f"Requisicao Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. {registro.nome} Status: {registro.status} criar Requisição"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    

    return redirect('ceoListViews')
    
    
#------------------------------------------------------


#------------------------------------------------------
from django.http import HttpResponse
def configurado_expedicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')

def expedicao_expedido(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')

def expedicao_expedido2(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')


def expedir_requisicao(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')
def expedir_requisicaotec(request, id):
    registro = get_object_or_404(Requisicoes, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('tecnicoListView')

def expedir_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    # Alterar o status do registro para "Configurado"
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')






def configurado_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Configurado'
    registro.save()
    return redirect('ConfiguracaoListView')


def expedicao_expedido_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Enviado para o Cliente'
    registro.save()
    return redirect('expedicaoListViews')


#------------------------------------------------------
# View para aprovar uma requisição pela diretoria
#------------------------------------------------------
def Reprovar_diretoria(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Reprovado pela Diretoria'
    registro.save()
    return redirect('diretoriaListViews')
   

# View para reprovar uma requisição pela diretoria
def Aprovar_diretoria(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Aprovado pela Diretoria'  # Corrigido para "Aprovado pela Diretoria"
    registro.save()

    subject = f"Manutenção Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. {registro.nome} Status: {registro.status} criar Requisição"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    

    return redirect('diretoriaListViews')


#------------------------------------------------------
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from .models import Requisicoes

def gerar_pdf_requisicao(requisicao):
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'requisicao-{requisicao.id}.pdf')
    p = canvas.Canvas(pdf_path, pagesize=letter)
    p.setTitle(f'Requisição - {requisicao.id}')

    # Cabeçalho
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))
    y_position = 750
    p.drawString(200, y_position, "Protocolo de Requisição")
    y_position -= 30

    # Adicionar imagens de cabeçalho
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width, image_height = 150, 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20
    x_position = (page_width - total_width) / 2

    # Desenhar as imagens
    p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height, mask='auto')
    p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height, mask='auto')
    y_position -= (image_height + 20)

    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    def draw_text(p, theme, value, x, y, max_width):
        theme_style = ParagraphStyle('ThemeStyle', fontName='Helvetica-Bold', fontSize=12)
        value_style = ParagraphStyle('ValueStyle', fontName='Helvetica', fontSize=12)
        
        theme_paragraph = Paragraph(f"<b>{theme}</b>", theme_style)
        value_paragraph = Paragraph(value, value_style)
        
        theme_width, theme_height = theme_paragraph.wrap(max_width, y)
        value_width, value_height = value_paragraph.wrap(max_width, y)
        
        theme_paragraph.drawOn(p, x, y - theme_height)
        y -= theme_height
        value_paragraph.drawOn(p, x, y - value_height)
        y -= value_height + 1  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 30:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 650  # Reset y_position for the new page
        return y_position

    def safe_draw_text(p, theme, value, x, y, max_width):
        return draw_text(p, theme, str(value), x, y, max_width)

    def add_text_with_check(p, theme, value, x, y, max_width):
        required_space = 20  # Espaço necessário para cada entrada de texto
        y = check_space(p, y, required_space)
        return safe_draw_text(p, theme, value, x, y, max_width)

    def add_text_pair(p, theme1, value1, theme2, value2, x, y, max_width):
        y = add_text_with_check(p, theme1, value1, x, y, max_width)
        y = add_text_with_check(p, theme2, value2, x + max_width, y + 15, max_width)
        return y - 15

    x_positions = [100, 150]
    fields = [
        
    ("Nome:", requisicao.nome),
    ("Registro #:", requisicao.id),
    ("Endereço:", requisicao.endereco),
    ("Contrato:", requisicao.contrato),
    ("CNPJ:", requisicao.cnpj),
    ("Data:", requisicao.data.strftime("%d/%m/%Y") if requisicao.data else "N/A"),
    ("Motivo:", requisicao.motivo),
    ("Taxa de Envio:", requisicao.taxa_envio),
    ("Comercial:", requisicao.comercial),
    ("Tipo de Produto:", requisicao.tipo_produto),
    ("Carregador:", requisicao.carregador),
    ("Cabo:", requisicao.cabo),
    ("TP:", requisicao.TP),
    ("Envio:", requisicao.envio),
    ("Quantidade:", requisicao.numero_de_equipamentos),
    ("Valor Unitário:", requisicao.valor_unitario),
    ("Aos Cuidados:", requisicao.aos_cuidados),
    ("Customização:", requisicao.tipo_customizacao),

    ]

    for i in range(0, len(fields), 2):
        theme1, value1 = fields[i]
        theme2, value2 = fields[i + 1] if i + 1 < len(fields) else ("   ", "   ")
        y_position = add_text_pair(p, theme1, value1, theme2, value2, x_positions[0], y_position, 300)

    # Adicionar ID Equipamentos com verificação de comprimento
    equipamentos = str(requisicao.id_equipamentos)
    if len(equipamentos) > 800:
        # Se o número de caracteres exceder 1200, comece uma nova página
        p.showPage()
        p.setFont("Helvetica", 12)
        p.setFillColor(colors.black)
        y_position = 750  # Reset y_position for new page

    y_position = add_text_with_check(p, "ID Equipamentos:", equipamentos, 100, y_position, 500)

    # Finalize the PDF
    p.showPage()
    p.save()
    return pdf_path

def enviar_email_com_pdf(request, id):
    requisicao = get_object_or_404(Requisicoes, id=id)
    pdf_path = gerar_pdf_requisicao(requisicao)
    
    subject = f"Requisição Criada: {requisicao.id}"
    message = f"A requisição {requisicao.id} foi criada com sucesso. Segue PDF para tratativa."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach_file(pdf_path)
    
    try:
        email.send()
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    return redirect('requisicoesListView')


from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Requisicoes

def download_pdf_requisicao(request, id):
    requisicao = get_object_or_404(Requisicoes, id=id)
    pdf_path = gerar_pdf_requisicao(requisicao)
    
    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="requisicao-{requisicao.id}.pdf"'


        return response
from django.db import transaction
from django.db.models import F
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import estoque_antenista
from .forms import EstoqueantenistarForm
class RegistrarEstoqueantenistaView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = estoque_antenista
    form_class = EstoqueantenistarForm
    template_name = 'estoque_antenista.html'
    success_url = reverse_lazy('RegistrarEstoqueantenistaView')
    permission_required = 'tuper.add_estoque_tuper'

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        tipo_produto = form.cleaned_data['tipo_produto']
        quantidade = form.cleaned_data['quantidade'] // 2  # Retira metade do valor adicionado
        endereco = form.cleaned_data['endereco']

        with transaction.atomic():
            estoques = estoque_antenista.objects.filter(nome=nome, tipo_produto=tipo_produto)
            if estoques.exists():
                estoque = estoques.order_by('-quantidade').first()
                estoque.quantidade = F('quantidade') + quantidade
                estoque.endereco = endereco
                estoque.save(update_fields=['quantidade', 'endereco'])
            else:
                estoque = estoque_antenista(nome=nome, tipo_produto=tipo_produto, quantidade=quantidade, endereco=endereco)
                estoque.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estoques = estoque_antenista.objects.all()
        estoque_dict = {}

        for estoque in estoques:
            key = (estoque.nome, estoque.tipo_produto)
            if key in estoque_dict:
                estoque_dict[key].quantidade += estoque.quantidade
            else:
                estoque_dict[key] = estoque

        for key, estoque in estoque_dict.items():
            estoque.save()
            estoque_antenista.objects.filter(nome=key[0], tipo_produto=key[1]).exclude(id=estoque.id).delete()

        context['estoques'] = list(estoque_dict.values())
        return context