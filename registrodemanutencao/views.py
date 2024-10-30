

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from .models import registrodemanutencao
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from django.core.mail import send_mail
from django.contrib.auth.mixins import  PermissionRequiredMixin,LoginRequiredMixin 
# Importações dos modelos e formulários
from .models import registrodemanutencao, ImagemRegistro,retorno
from requisicao.models import Requisicoes
from .forms import FormulariosForm, FormulariosUpdateForm,ImagemRegistroFormSet, registrodemanutencao
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from.forms import RetornoForm
# View para listar todos os registros de manutenção com paginação.4
#-----------------------------------------------------------------------
class entradasListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = registrodemanutencao
    template_name = "registro_das_entradas.html"
    context_object_name = 'dasentradas'
    
    permission_required = 'registrodemanutencao.view_registrodemanutencao'

    def get_queryset(self):
        queryset = registrodemanutencao.objects.filter(
            status__in=['Pendente', 'Manutenção', 'Reprovado pela Inteligência', 'Aprovado pela Diretoria']
        )

        id_param = self.request.GET.get('id')
        nome_param = self.request.GET.get('nome')
        status_param = self.request.GET.get('status')

        if id_param:
            queryset = queryset.filter(id=id_param)  # Filtra pelo ID
        if nome_param:
            queryset = queryset.filter(nome__nome__icontains=nome_param)
        if status_param:
            queryset = queryset.filter(status=status_param)
        queryset =queryset.order_by('-id')

        return queryset
#----------------------------------------------------------------------------

class FormularioListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = registrodemanutencao
    template_name = "registrodemanutencaolist.html"
    context_object_name = 'registrodemanutencao'
    paginate_by = 6
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome', '')
        status = self.request.GET.get('status', '')
        
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if status:
            queryset = queryset.filter(status=status)
       
        return queryset

#------------------------------------------------------------------------------
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import registrodemanutencao
from .forms import FormulariosForm

class FormulariosCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = registrodemanutencao
    form_class = FormulariosForm
    template_name = 'registrodemanutencao_create.html'
    success_url = reverse_lazy('FormulariosCreateView')
    permission_required = 'registrodemanutencao.add_registrodemanutencao'

    def form_valid(self, form):
        form.instance.quantidade = self.request.POST.get('quantidade', 0)
        return super().form_valid(form)




# View para atualizar um registro de manutenção existente.
class FormulariosUpdateView(LoginRequiredMixin,  UpdateView):
    model = registrodemanutencao
    form_class = FormulariosUpdateForm
    template_name = 'registrodemanutencao_update.html'
    success_url = reverse_lazy('entradasListView')
     # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, request.FILES, instance=self.object)
        imagens_formset = ImagemRegistroFormSet(request.POST, request.FILES, instance=self.object)

        if form.is_valid() and imagens_formset.is_valid():
            return self.form_valid(form, imagens_formset)
        else:
            return self.form_invalid(form, imagens_formset)

    def form_valid(self, form, imagens_formset):
        self.object = form.save()
        imagens_formset.instance = self.object
        imagens_formset.save()
        return redirect(self.success_url)

    def form_invalid(self, form, imagens_formset):
        return render(self.request, self.template_name, {
            'form': form,
            'imagens_formset': imagens_formset
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['imagens_formset'] = ImagemRegistroFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['imagens_formset'] = ImagemRegistroFormSet(instance=self.object)
        return context
    
    

class FormularioDetailView(LoginRequiredMixin,  DetailView):
    model = registrodemanutencao
    template_name = 'registrodemanutencao_detail.html'
    context_object_name = 'registrodemanutencao_detail'
     # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

# View para deletar um registro de manutenção.
#-------------------------------------------------------------------------

def aprovar_manut(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Aprovado Inteligência'
    registro.save()
    
    subject = f"Manutenção Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. segue pdf para tratativa "
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    try:
        send_mail(subject, message, from_email, recipient_list)
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    return redirect('entradasListView')

def reprovar_manut(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Manutenção'
    registro.save()
    return redirect('entradasListView')

# View para listar registros de manutenção filtrados pelo status 'Aprovado', 'Reprovado' ou 'Pendente'.

#--------------------------------------

class ConfiguracaoListView(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = 'configuracao_list.html'
    context_object_name = 'registros'
    paginate_by = 6
    success_url = reverse_lazy('configuracao_list')
    permission_required = 'registrodemanutencao.view_registrodemanutencao' 
     # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = registrodemanutencao()
        return context
#--------------------------------------

class expedicaoListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = Requisicoes
    template_name = 'expedicao_list.html'  # Nome do seu template para status "configuração"
    context_object_name = 'requisicoes'
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            Q(status__iexact='Expedido') | Q(status__iexact='Aprovado')
        )
        print(queryset.query)  # Isso imprimirá a consulta SQL no console
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicione os registros de manutenção ao contexto
        context['registros_manutencao'] = registrodemanutencao.objects.filter(
            Q(status__iexact='Expedido') | Q(status__iexact='Aprovado')
        )
        return context

#-----------------------------------------------------------------------------------

# View para exibir os detalhes de uma expedição específica.
class expedicaoDetailView( PermissionRequiredMixin,LoginRequiredMixin , DetailView):
    model = ImagemRegistro
    template_name = 'expedicao_detail.html'
    context_object_name = 'expedicoes'
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo

# View para exibir os detalhes de uma configuração específica.
class configDetailView(LoginRequiredMixin, DetailView):
    model = registrodemanutencao
    template_name = 'config_detail.html'
    context_object_name = 'config_detail'
      # Substitua 'registrodemanutencao' pelo nome do seu aplicativo






from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Table
from reportlab.lib.styles import ParagraphStyle
import os
from django.conf import settings

def download_protocolo_entrada(request, pk):
    try:
        registro = registrodemanutencao.objects.get(pk=pk)
    except registrodemanutencao.DoesNotExist:
        return HttpResponse("Registro não encontrado.", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="registro-manutencao-{pk}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle(f'Protocolo de entrada - {pk}')

    # Cabeçalho
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))
    y_position = 750
    p.drawString(200, y_position, "Protocolo de entrada")
    y_position -= 30

    # Adicionar imagens de cabeçalho
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width, image_height = 150, 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20
    x_position = (page_width - total_width) / 2

    # Desenhar as imagens sem o retângulo branco
    p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height, mask='auto')
    p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height, mask='auto')
    y_position -= (image_height + 50)

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
        y -= value_height + 15  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    def safe_draw_text(p, theme, value, x, y, max_width):
        if isinstance(value, str):
            return draw_text(p, theme, value, x, y, max_width)
        else:
            return draw_text(p, theme, str(value), x, y, max_width)

    def add_text_with_check(p, theme, value, x, y, max_width):
        required_space = 50  # Espaço necessário para cada entrada de texto
        y = check_space(p, y, required_space)
        return safe_draw_text(p, theme, value, x, y, max_width)
    
    def add_text_pair(p, theme1, value1, theme2, value2, x, y, max_width):
        y = add_text_with_check(p, theme1, value1, x + 250, y, max_width)
        y = add_text_with_check(p, theme2, value2, x, y + 60, max_width)
        return y - 35

    x_positions = [100, 350]
    fields = [

        ("Registro #:", registro.id),
        ("Nome:", registro.nome),
        ("Data:", registro.data_criacao),
        ("Tipo de Entrada:", registro.tipo_entrada),
        ("Tipo de Produto:", registro.tipo_produto),
        ("Motivo:", registro.motivo),
        ("Tipo Customização:", registro.tipo_customizacao),
        ("Entregue por/Retirado por:", registro.entregue_por_retirado_por),
        ("Recebimento:", registro.recebimento),
        ("Faturamento:", registro.faturamento),
        
        ("Customização:", registro.customizacaoo),
        ("Tratativa:", registro.tratativa),
        ("Status:", registro.status)
    ]

    for i in range(0, len(fields), 2):
        theme1, value1 = fields[i]
        theme2, value2 = fields[i + 1] if i + 1 < len(fields) else ("", "")
        y_position = add_text_pair(p, theme1, value1, theme2, value2, x_positions[0], y_position, 200)

    # Adicionar Número Equipamento no centro com tamanho h3
    p.setFont("Helvetica-Bold", 18)
    p.drawCentredString(page_width / 2, y_position - 50, "IDS DOS EQUIPAMENTOS")
    p.setFont("Helvetica", 12)
    y_position -= 80

    # Dividir os números dos equipamentos em grupos de 8
    try:
        equipamentos = sorted(map(int, (num.strip() for num in registro.numero_equipamento.split() if num.strip())))
    except ValueError:
        return HttpResponse("Número de equipamento inválido fornecido.", status=400)

    equipment_grid = [equipamentos[i:i+8] for i in range(0, len(equipamentos), 8)]

    # Criando a tabela para os números dos equipamentos
    equipment_table_data = []
    for group in equipment_grid:
        row = [str(num) for num in group]  # Convertendo os números para strings
        equipment_table_data.append(row)

    # Adicionando a tabela ao PDF
    equipment_table = Table(equipment_table_data)
    equipment_table.wrapOn(p, page_width, page_height)
    equipment_table.drawOn(p, 30, y_position - 10)

    # Feche o objeto PDF e entregue o PDF ao navegador.
    p.showPage()
    p.save()
    return response



from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import os
from django.conf import settings










def download_pdf(request, pk):
    try:
        registro = registrodemanutencao.objects.get(pk=pk)
    except registrodemanutencao.DoesNotExist:
        return HttpResponse("Registro não encontrado.", status=404)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="registro-manutencao-{pk}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setTitle(f'Protocolo de Manutenção - {pk}')

    # Cabeçalho
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))
    y_position = 750
    p.drawString(200, y_position, "Relatório de Manutenção")
    y_position -= 10

    # Adicionar imagens de cabeçalho
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width, image_height = 150, 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20
    x_position = (page_width - total_width) / 2

    # Desenhar as imagens sem o retângulo branco
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
        y -= value_height + 10  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    def safe_draw_text(p, theme, value, x, y, max_width):
        if isinstance(value, str):
            return draw_text(p, theme, value, x, y, max_width)
        else:
            return draw_text(p, theme, str(value), x, y, max_width)

    def add_text_with_check(p, theme, value, x, y, max_width):
        required_space = 50  # Espaço necessário para cada entrada de texto
        y = check_space(p, y, required_space)
        return safe_draw_text(p, theme, value, x, y, max_width)

    def draw_image(p, image_path, x, y, width, height):
        if y - height < 50:
            p.showPage()
            y = 750
        p.drawImage(image_path, x, y - height, width=width, height=height)
        return y - height - 10  # Espaçamento entre imagens

    y_position = add_text_with_check(p, "Registro #:", registro.id, 50, y_position, 400)
    y_position = add_text_with_check(p, "Data:", registro.data_criacao.strftime("%d/%m/%Y"), 50, y_position, 400)
    y_position = add_text_with_check(p, "Nome:", registro.nome, 50, y_position, 400)
    y_position = add_text_with_check(p, "Tipo de Entrada:", registro.tipo_entrada, 50, y_position, 400)
    y_position = add_text_with_check(p, "Tipo de Produto:", registro.tipo_produto, 50, y_position, 400)
    y_position = add_text_with_check(p, "Motivo:", registro.motivo, 50, y_position, 400)
    y_position = add_text_with_check(p, "Customização:", registro.customizacaoo, 50, y_position, 400)
    
    y_position = add_text_with_check(p, "Entregue por/Retirado por:", registro.entregue_por_retirado_por, 50, y_position, 400)
    y_position = add_text_with_check(p, "Recebimento:", registro.recebimento, 50, y_position, 400)
    y_position = add_text_with_check(p, "Faturamento:", registro.faturamento, 50, y_position, 400)
    y_position = add_text_with_check(p, "Setor:", registro.setor, 50, y_position, 400)
    y_position = add_text_with_check(p, "Número Equipamento:", registro.numero_equipamento, 50, y_position, 400)
    y_position = add_text_with_check(p, "observacoes:", registro.observacoes, 50, y_position, 400)
    y_position = add_text_with_check(p, "Tratativa:", registro.tratativa, 50, y_position, 400)
  

    # Iterar sobre todas as imagens relacionadas e desenhá-las no PDF
    for imagem in registro.imagens.all():
        if imagem.imagem:  # Verifique se a imagem existe
            y_position = add_text_with_check(p, "ID:", f"{imagem.id} - ID equipamento: {imagem.id_equipamento} - Tipo Problema: {imagem.tipo_problema}", 100, y_position, 400)
            # Adicionar lógica para escrever texto explicativo no campo "tratativa"
            if imagem.tipo_problema == "Oxidação":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Para resolver o problema do equipamento,
                foram realizadas as tratativas necessárias e alguns testes posteriores, porém,
                sem sucesso, sendo assim será necessária a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico. 
                """
            elif imagem.tipo_problema == "Placa Danificada":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Para resolver o problema do equipamento,
                foram realizadas as tratativas necessárias e alguns testes
                posteriores, porém, sem sucesso, 
                sendo assim será necessária a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico
                """
            elif imagem.tipo_problema == "Placa danificada SEM CUSTO":
                texto_tratativa = """A placa do equipamento está danificada, 
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "USB Danificado":
                texto_tratativa ="""
                Sobre a Manutenção Realizada:
                Para resolver o problema do equipamento, 
                foram realizadas as tratativas necessárias e alguns testes posteriores,
                porém, sem sucesso, sendo assim será necessária a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico.
                """
            elif imagem.tipo_problema == "USB Danificado SEM CUSTO":
                texto_tratativa = """A porta USB do equipamento está danificada,
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "Botão de acionamento Danificado":
                texto_tratativa = """O botão de acionamento do equipamento está danificado, 
                dificultando seu uso."""
            elif imagem.tipo_problema == "Botão de acionamento Danificado SEM CUSTO":
                texto_tratativa = """O botão de acionamento do equipamento está danificado,
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "Antena LoRa Danificada":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Diante deste diagnóstico e após as tratativas, 
                afirmamos que será necessário a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico
                """
            elif imagem.tipo_problema == "Sem problemas Identificados":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Gostaríamos de informar que concluímos com sucesso as manutenções necessárias no equipamento
                que nos foi confiado para reparo. Após uma análise cuidadosa,
                identificamos e corrigimos os problemas que estavam impactando o seu funcionamento adequado.
                Atenciosamente,
                Laboratório Técnico.
                """
            else:
                texto_tratativa = "Descrição genérica para problemas não especificados."

            y_position = add_text_with_check(p, "Tratativa:", texto_tratativa, 100, y_position, 400)
                        # Desenhe a imagem
            caminho_imagem = os.path.join(settings.MEDIA_ROOT, str(imagem.imagem))
            if y_position - 100 < 50:  # Verifique se há espaço suficiente para a imagem na página atual
                p.showPage()  # Crie uma nova página se necessário
                y_position = 750  # Redefina a posição Y para o topo da nova página
            p.drawImage(caminho_imagem, 100, y_position - 100, width=200, height=100)
            y_position -= 120

    # Feche o objeto PDF e entregue o PDF ao navegador.
    p.showPage()
    p.save()
    return response


class CriarRetornoView(CreateView):
    model = retorno
    form_class = RetornoForm
    template_name = 'criar_retorno.html'
    

    def form_valid(self, form):
        self.object = form.save()
        return redirect('download_pdf', pk=self.object.pk)

class DownloadPDFView(DetailView):
    model = retorno

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="registro-manutencao-{self.object.pk}.pdf"'

        p = canvas.Canvas(response, pagesize=letter)
        p.setTitle(f'Registro de Manutenção - {self.object.pk}')

        # Defina as fontes e cores
        p.setFont("Helvetica-Bold", 16)
        p.setFillColor(colors.HexColor("#004B87"))

        # Cabeçalho
        y_position = 750
        p.drawString(100, y_position, "Relatório de Manutenção")
        y_position -= 30

        # Adicionar as imagens lado a lado com fundo branco
        imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
        imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
        image_width = 200
        image_height = 100
        page_width, page_height = letter
        total_width = image_width * 2 + 20  # Largura total das duas imagens com um espaço entre elas
        x_position = (page_width - total_width) / 2

        # Desenhar um retângulo branco como fundo para as imagens
        p.setFillColor(colors.white)
        p.rect(x_position - 10, y_position - image_height - 10, total_width + 20, image_height + 20, fill=1)

        # Desenhar a primeira imagem
        p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height)
        # Desenhar a segunda imagem ao lado da primeira
        p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height)
        y_position -= (image_height + 20)

        # Adicionar a imagem do campo 'imagem' do modelo 'retorno'
        if self.object.imagem:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.object.imagem))
            p.drawImage(image_path, 100, y_position - 200, width=200, height=200)
            y_position -= 220

        # Restaurar a fonte para o conteúdo principal
        p.setFont("Helvetica", 12)
        p.setFillColor(colors.black)

        #   # Desenhe o conteúdo do PDF
        p.drawString(100, y_position, f"Cliente: {self.object.cliente}")
        y_position -= 20
        p.drawString(100, y_position, f"Produto: {self.object.produto}")
        y_position -= 20
        p.drawString(100, y_position, f"Tipo de Problema: {self.object.tipo_problema}")
        y_position -= 20
        p.drawString(100, y_position, f"ID Equipamentos: {self.object.id_equipamentos}")
        y_position -= 20
       

        # Feche o objeto PDF e entregue o PDF ao navegador.
        p.showPage()
        p.save()
        return response


class ListaRetornosView(ListView):
    model = retorno
    template_name = 'lista_retornos.html'
    context_object_name = 'retornos'





def minha_view(request):
    if request.method == 'POST':
        form = FormulariosUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alguma_url_de_sucesso')
    else:
        form = FormulariosUpdateForm()
    return render(request, 'meu_template.html', {'form': form})
# Função para aprovar um registro de manutenção.


class historico_manutencaoListView( PermissionRequiredMixin,LoginRequiredMixin , ListView):
    model = registrodemanutencao
    template_name = 'historico_manutencao.html'  # Nome do seu template para status "configuração"
    context_object_name = 'dasentradas'
    paginate_by = 12 
    permission_required = 'registrodemanutencao.view_registrodemanutencao'  # Substitua 'registrodemanutencao' pelo nome do seu aplicativo
    
    def get_queryset(self):
        queryset = registrodemanutencao.objects.all()
        nome = self.request.GET.get('nome')
        retornoequipamentos = self.request.GET.get('retornoequipamentos')
        
        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        
        if retornoequipamentos:
            queryset = queryset.filter(retornoequipamentos__icontains=retornoequipamentos)
        
        
        return queryset


def clean_id_equipamentos(self):
        data = self.cleaned_data['id_equipamentos']
        if len(data) > 6:
            data = data[6:]  # Remove os primeiros 6 caracteres
        return data



from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
@login_required
def aprovar_manutencao(request, id):
    registro = get_object_or_404(registrodemanutencao, id=id)
    registro.status = 'Comercial'
    registro.save()
    
    subject = f"Manutenção Aprovada: {registro.id}"
    message = f"A manutenção {registro.id} foi aprovada com sucesso. Segue PDF para tratativa."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = ['sjuniorr6@gmail.com']
    
    # Gerar o PDF
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'registro-manutencao-{registro.id}.pdf')
    p = canvas.Canvas(pdf_path, pagesize=letter)
    p.setTitle(f'Registro de Manutenção - {registro.id}')

    # Cabeçalho
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.HexColor("#004B87"))
    y_position = 750
    p.drawString(100, y_position, "Relatório de Manutenção")
    y_position -= 30

    # Adicionar imagens de cabeçalho
    imagem_padrao = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/SIDNEISIDNEISIDNEI.png')
    imagem_qrcode = os.path.join(settings.MEDIA_ROOT, 'imagens_registros/qrcode.png')
    image_width, image_height = 200, 100
    page_width, page_height = letter
    total_width = image_width * 2 + 20
    x_position = (page_width - total_width) / 2

    p.setFillColor(colors.white)
    p.rect(x_position - 10, y_position - image_height - 10, total_width + 20, image_height + 20, fill=1)
    p.drawImage(imagem_padrao, x_position, y_position - image_height, width=image_width, height=image_height)
    p.drawImage(imagem_qrcode, x_position + image_width + 20, y_position - image_height, width=image_width, height=image_height)
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
        y -= value_height + 10  # Espaçamento entre linhas
        
        return y

    def check_space(p, y_position, required_space):
        if y_position - required_space < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            p.setFillColor(colors.black)
            return 750
        return y_position

    def safe_draw_text(p, theme, value, x, y, max_width):
        if isinstance(value, str):
            return draw_text(p, theme, value, x, y, max_width)
        else:
            return draw_text(p, theme, str(value), x, y, max_width)

    def add_text_with_check(p, theme, value, x, y, max_width):
        required_space = 50  # Espaço necessário para cada entrada de texto
        y = check_space(p, y, required_space)
        return safe_draw_text(p, theme, value, x, y, max_width)

    def draw_image(p, image_path, x, y, width, height):
        if y - height < 50:
            p.showPage()
            y = 750
        p.drawImage(image_path, x, y - height, width=width, height=height)
        return y - height - 10  # Espaçamento entre imagens

    y_position = add_text_with_check(p, "Nome:", registro.nome, 100, y_position, 400)
    y_position = add_text_with_check(p, "Tipo de Entrada:", registro.tipo_entrada, 100, y_position, 400)
    y_position = add_text_with_check(p, "Tipo de Produto:", registro.tipo_produto, 100, y_position, 400)
    
    y_position = add_text_with_check(p, "Motivo:", registro.motivo, 100, y_position, 400)
    y_position = add_text_with_check(p, "Tipo Customização:", registro.tipo_customizacao, 100, y_position, 400)
    y_position = add_text_with_check(p, "Entregue por/Retirado por:", registro.entregue_por_retirado_por, 100, y_position, 400)
    y_position = add_text_with_check(p, "Recebimento:", registro.recebimento, 100, y_position, 400)
    y_position = add_text_with_check(p, "Faturamento:", registro.faturamento, 100, y_position, 400)
    y_position = add_text_with_check(p, "Setor:", registro.setor, 100, y_position, 400)
    y_position = add_text_with_check(p, "Customização:", registro.customizacaoo, 100, y_position, 400)
    y_position = add_text_with_check(p, "Número Equipamento:", registro.numero_equipamento, 100, y_position, 400)
    y_position = add_text_with_check(p, "Tratativa:", registro.tratativa, 100, y_position, 400)
    y_position = add_text_with_check(p, "Status:", registro.status, 100, y_position, 400)

    # Iterar sobre todas as imagens relacionadas e desenhá-las no PDF
    for imagem in registro.imagens.all():
        if imagem.imagem:  # Verifique se a imagem existe
            y_position = add_text_with_check(p, "ID:", f"{imagem.id} - ID EQUIPAMENTO: {imagem.id_equipamento} - Tipo Problema: {imagem.tipo_problema}", 100, y_position, 400)

            # Adicionar lógica para escrever texto explicativo no campo "tratativa"
            if imagem.tipo_problema == "Oxidação":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Para resolver o problema do equipamento,
                foram realizadas as tratativas necessárias e alguns testes posteriores, porém,
                sem sucesso, sendo assim será necessária a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico. 
                """
            elif imagem.tipo_problema == "Placa Danificada":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Para resolver o problema do equipamento,
                foram realizadas as tratativas necessárias e alguns testes
                posteriores, porém, sem sucesso, 
                sendo assim será necessária a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico
                """
            elif imagem.tipo_problema == "Placa danificada SEM CUSTO":
                texto_tratativa = """A placa do equipamento está danificada, 
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "USB Danificado":
                texto_tratativa ="""
                Sobre a Manutenção Realizada:
                Para resolver o problema do equipamento, 
                foram realizadas as tratativas necessárias e alguns testes posteriores,
                porém, sem sucesso, sendo assim será necessária a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico.
                """
            elif imagem.tipo_problema == "USB Danificado SEM CUSTO":
                texto_tratativa = """A porta USB do equipamento está danificada,
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "Botão de acionamento Danificado":
                texto_tratativa = """O botão de acionamento do equipamento está danificado, 
                dificultando seu uso."""
            elif imagem.tipo_problema == "Botão de acionamento Danificado SEM CUSTO":
                texto_tratativa = """O botão de acionamento do equipamento está danificado,
                mas a reparação será realizada sem custo."""
            elif imagem.tipo_problema == "Antena LoRa Danificada":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Diante deste diagnóstico e após as tratativas, 
                afirmamos que será necessário a troca do dispositivo.
                Atenciosamente,
                Laboratório Técnico
                """
            elif imagem.tipo_problema == "Sem problemas Identificados":
                texto_tratativa = """
                Sobre a Manutenção Realizada:
                Gostaríamos de informar que concluímos com sucesso as manutenções necessárias no equipamento
                que nos foi confiado para reparo. Após uma análise cuidadosa,
                identificamos e corrigimos os problemas que estavam impactando o seu funcionamento adequado.
                Atenciosamente,
                Laboratório Técnico.
                """
            else:
                texto_tratativa = "Descrição genérica para problemas não especificados."

            y_position = add_text_with_check(p, "Tratativa:", texto_tratativa, 100, y_position, 400)
            # Desenhe a imagem
            caminho_imagem = os.path.join(settings.MEDIA_ROOT, str(imagem.imagem))
            if y_position - 100 < 50:  # Verifique se há espaço suficiente para a imagem na página atual
                p.showPage()  # Crie uma nova página se necessário
                y_position = 750  # Redefina a posição Y para o topo da nova página
            p.drawImage(caminho_imagem, 100, y_position - 100, width=200, height=100)
            y_position -= 120

    # Feche o objeto PDF e salve no caminho especificado.
    p.showPage()
    p.save()

    # Enviar e-mail com o PDF anexado
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.attach_file(pdf_path)
    
    try:
        email.send()
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    
    return redirect('entradasListView')

@login_required
def reprovar_manutencao(request, id):  # Alterar o nome da função para corresponder ao URL
    requisicao = get_object_or_404(registrodemanutencao, id=id)
    requisicao.status = 'Manutenção'  # Certifique-se de que este é o status correto
    requisicao.save()
    return redirect('entradasListView')
def editado_manutencao(request, pk):  # O nome da função está correto
    requisicao = get_object_or_404(registrodemanutencao, id=pk)  # Use 'pk' aqui
    requisicao.status = 'Manutenção'  # Verifique se este é o status correto
    requisicao.save()
    return redirect('entradasListView') 


@login_required
def reprovar_manutencao2(request, id):  # Alterar o nome da função para corresponder ao URL
    requisicao = get_object_or_404(registrodemanutencao, id=id)
    requisicao.status = 'Reprovado pela Inteligência'  # Certifique-se de que este é o status correto
    requisicao.save()
    return redirect('entradasListView')

# Função decorada com @login_required para garantir que apenas usuários autenticados possam acessá-la.
@login_required
def rejeitadas(request, id):
    manutencao = get_object_or_404(registrodemanutencao, id=id)
    manutencao.status = 'Aprovado'
    manutencao.save()
    return redirect('rejeitadas')

# Função para renderizar o formulário de manutenção.
@login_required
def formulariom_view(request):
    return render(request, 'registrodemanutencao.html')

# Função para listar registros de manutenção.
@login_required
def manutencaolist(request):
    return render(request, 'manutencao_list.html')
