
from django.urls import path
from .views import formulariorateview, AcompanhamentoListView, formListView,agenteCreateView,agentesListView,get_agente_data,agenteUpdateView

urlpatterns = [
    path('formacompanhamento/create/', formulariorateview.as_view(), name='formacompanhamento'),
    path('facomp/', AcompanhamentoListView.as_view(), name='facomp'),
    path('agentesListView/', agentesListView.as_view(), name='agentesListView'),
    path('agenteUpdateView/<int:pk>/update/', agenteUpdateView.as_view(), name='agenteUpdateView'),
    path('agentes/', agenteCreateView.as_view(), name='agenteCreateView'),
    path('formacompanhamento/detail/', formListView.as_view(), name='formacompanhamento_detail'),
     path('get_agente_data/<int:agente_id>/', get_agente_data, name='get_agente_data'),
]