from django.shortcuts import render
from django.urls import reverse_lazy
from .models import paradasegura, passagemmodel
from .forms import paradaForm,PassagemModelForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse

class paradaCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = paradasegura
    template_name = 'parada_create.html'
    form_class = paradaForm
    success_url = reverse_lazy('paradaseguraform')
    permission_required = "parada.add_paradasegura"

class passagemCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = passagemmodel
    template_name = 'passagem.html'
    form_class = PassagemModelForm
    success_url = reverse_lazy('passagemCreateView')
    permission_required = "parada.add_paradasegura"

    


from django.views.generic import ListView
from .models import passagemmodel

class PassagemListView(ListView):
    model = passagemmodel
    template_name = 'historico_passagem.html'
    context_object_name = 'passagens'
    paginate_by = 10  # Defina quantas entradas por página você deseja

    def get_queryset(self):
        return passagemmodel.objects.all().order_by('-data_criacao') 

class paradaListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = paradasegura
    template_name = 'pa_list.html'
    context_object_name = 'pa'
    paginate_by = 12
    permission_required = 'parada.view_paradasegura'

    def get_queryset(self):
        return paradasegura.objects.all().order_by('-id') 
    

from django.http import JsonResponse

def get_choices(request):
    tipo_posto = request.GET.get('tipo_posto')
    print(f'Tipo de posto: {tipo_posto}')  # Debugging
    response_data = {
        'iscas': [],
        'cadeados': [],
        'pa': []
    }

    if tipo_posto:
        if tipo_posto in paradasegura.POSTOS_INFO1:
            iscas = paradasegura.POSTOS_INFO1[tipo_posto].get('iscas', [])
            cadeados = paradasegura.POSTOS_INFO1[tipo_posto].get('cadeados', [])
            response_data['iscas'] = iscas
            response_data['cadeados'] = cadeados
            print(f'Iscas: {iscas}, Cadeados: {cadeados}')  # Debugging

        if tipo_posto in paradasegura.POSTOS_INFO2:
            pa = paradasegura.POSTOS_INFO2[tipo_posto].get('pa', [])
            response_data['pa'] = pa
            print(f'PA: {pa}')
    return JsonResponse(response_data)

def get_pa_choices(request):
    tipo_posto = request.GET.get('tipo_posto')
    print(f'Tipo de posto: {tipo_posto}')  # Debugging
    if tipo_posto and tipo_posto in passagemmodel.POSTOS_INFO2:
        pa = passagemmodel.POSTOS_INFO2[tipo_posto]['pa']
        print(f'PA: {pa}')  # Debugging
        return JsonResponse({
            'pa': pa,
        })
    return JsonResponse({'pa': []})