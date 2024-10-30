from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Qualit
from .forms import QualitForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class QualitCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Qualit
    form_class = QualitForm
    template_name = 'criar_qualit.html'
    success_url = reverse_lazy('criar_qualit')
    permission_required = 'qualit.add_qualit'  # Substitua 'qualit' pelo nome do seu aplicativo

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # Adicione esta linha para imprimir os erros do formulário
        return super().form_invalid(form)

class QualitListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Qualit
    template_name = 'listar_qualits.html'
    context_object_name = 'qualits'
    permission_required = 'qualit.view_qualit'  # Substitua 'qualit' pelo nome do seu aplicativo

    def get_queryset(self):
        queryset = super().get_queryset()
        id_equipamento = self.request.GET.get('id_equipamento')
        iccid_novo = self.request.GET.get('iccid_novo')
        cliente = self.request.GET.get('cliente')
        
        if id_equipamento or iccid_novo or cliente:
            if id_equipamento:
                queryset = queryset.filter(id_equipamento=id_equipamento)
            if iccid_novo:
                queryset = queryset.filter(iccid_novo=iccid_novo)
            if cliente:
                queryset = queryset.filter(cliente__iexact=cliente)
        else:
            queryset = queryset.none()
        
        return queryset

@login_required
def qualit(request):
    return render(request, 'qualit.html')
