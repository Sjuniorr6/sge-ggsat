import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ReativacaoForm, IdIccidFormSet, IdIccidForm
from .models import Reativacao, IdIccid, Clientes
from django.views.generic import ListView
from requisicao.models import Requisicoes
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ReativacaoIdIccidCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reativacao.add_reativacao'  # Substitua 'reativacao' pelo nome do seu aplicativo

    def get(self, request):
        reativacao_form = ReativacaoForm()
        id_iccid_formset = IdIccidFormSet(queryset=IdIccid.objects.none())
        return render(request, 'reativacao_id_iccid_form.html', {
            'reativacao_form': reativacao_form,
            'id_iccid_formset': id_iccid_formset
        })

    def post(self, request):
        reativacao_form = ReativacaoForm(request.POST)
        id_iccid_formset = IdIccidFormSet(request.POST)

        if reativacao_form.is_valid() and id_iccid_formset.is_valid():
            reativacao = reativacao_form.save()

            # Contador para quantidade
            quantidade = 0

            # Processar campos adicionados dinamicamente
            for key, value in request.POST.items():
                if key.startswith('id_idiccid_set-') and key.endswith('-ccid_equipamentos'):
                    contador = key.split('-')[1]
                    ccid_equipamentos = value
                    id_equipamentos_key = f'id_idiccid_set-{contador}-id_equipamentos'
                    id_equipamentos = request.POST.get(id_equipamentos_key, "")

                    if ccid_equipamentos and id_equipamentos:
                        IdIccid.objects.create(
                            reativacao=reativacao,
                            ccid_equipamentos=ccid_equipamentos,
                            id_equipamentos=id_equipamentos,
                            quantidade=quantidade  # Armazenar a quantidade
                        )
                        quantidade += 1  # Incrementar a quantidade

                        # Fazer a reativação usando a API da 1nce
                        token = self.obter_token_acesso()
                        if token:
                            self.reativar_equipamento(ccid_equipamentos, token)

            return redirect('reativacao_id_iccid_adicionar')

        return render(request, 'reativacao_id_iccid_form.html', {
            'reativacao_form': reativacao_form,
            'id_iccid_formset': id_iccid_formset
        })

    def obter_token_acesso(self):
        url = "https://api.1nce.com/management-api/v1/oauth/token"
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        data = {
            "grant_type": "password",
            "username": "seu_usuario",
            "password": "sua_senha"
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            token = response.json().get("access_token")
            print("Token de acesso obtido com sucesso!")
            return token
        else:
            print(f"Erro ao obter token de acesso: {response.status_code}")
            print(response.text)
            return None

    def reativar_equipamento(self, ccid_equipamentos, token):
        url = "https://api.1nce.com/management-api/v1/sims"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        data = [
            {
                "imei_lock": False,
                "status": "Enabled",
                "ccid_equipamentos": ccid_equipamentos
            }
        ]

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("Equipamento reativado com sucesso!")
        else:
            print(f"Erro ao reativar equipamento: {response.status_code}")
            print(response.text)

from django.http import JsonResponse  # Importar JsonResponse se for necessário

class RequisicoesListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Requisicoes
    template_name = 'requisicoes_list.html'
    context_object_name = 'requisicoes'
    paginate_by = 5
    permission_required = 'reativacao.view_reativacao'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')  # Ordenação decrescente dos IDs
        nome = self.request.GET.get('nome')
        status = self.request.GET.get('status')

        if nome:
            queryset = queryset.filter(nome__nome__icontains=nome)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Reativacao, IdIccid, Clientes
from .forms import IdIccidForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.core.paginator import Paginator

class ReativacaoListView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'reativacao.view_reativacao'
    
    def get(self, request):
        cliente_filtro = request.GET.get('cliente_filtro')
        status_reativacao_filtro = request.GET.get('status_reativacao_filtro')
        motivo_reativacao_filtro = request.GET.get('motivo_filtro')
        
        reativacoes = Reativacao.objects.all().order_by('-id')

        if cliente_filtro:
            reativacoes = reativacoes.filter(nome__id=cliente_filtro)
        if status_reativacao_filtro:
            reativacoes = reativacoes.filter(status_reativacao=status_reativacao_filtro)
        if motivo_reativacao_filtro:
            reativacoes = reativacoes.filter(motivo_reativacao=motivo_reativacao_filtro)

        # Paginação
        paginator = Paginator(reativacoes, 10)  # 10 registros por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'reativacao_list.html', {
            'reativacoes': page_obj,  # Passando a página em vez da queryset completa
            'clientes_choices': Clientes.objects.all(),
            'status_reativacao_choices': Reativacao.STATUS_CHOICES,
            'motivos_choices': Reativacao.MOTIVO_CHOICES,
            'page_obj': page_obj,  # Adicionando page_obj ao contexto
        })

def update_status(request):
    if request.method == 'POST':
        id_iccid = request.POST.get('id_iccid')
        novo_status = request.POST.get('status')
        
        # Atualiza o status no banco de dados
        reativacao = Reativacao.objects.get(id=id_iccid)
        reativacao.status_reativacao = novo_status
        reativacao.save()

        return JsonResponse({'success': True, 'status': novo_status})

    return JsonResponse({'success': False, 'error': 'Método não permitido'})

    


@method_decorator(login_required, name='dispatch')
class ReativacaoView( PermissionRequiredMixin,LoginRequiredMixin, View):
    permission_required = 'reativacao.view_reativacao'
    paginate_by = 5
    def post(self, request):
        id_iccid = get_object_or_404(IdIccid, pk=request.POST.get('id_iccid'))
        status = request.POST.get('status_reativacao')
        if status:
            id_iccid.status = status
            id_iccid.save()
            return JsonResponse({'success': True, 'status': id_iccid.status})
        return JsonResponse({'success': False}, status=400) # Substitua 'reativacao' pelo nome do seu aplicativo

    def get(self, request):
        return render(request, 'reativacao.html')

from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
from .pdf_utils import gerar_pdf_id_iccid
from .models import IdIccid
import os


class DownloadPdfView(View):

    def get(self, request, id_iccid):
        id_iccid_obj = get_object_or_404(IdIccid, pk=id_iccid)
        pdf_path = gerar_pdf_id_iccid(id_iccid_obj)
        if os.path.exists(pdf_path):
            return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        else:
            # Handle the case where the PDF was not generated successfully
            return HttpResponse("Erro ao gerar o PDF", status=500)
        