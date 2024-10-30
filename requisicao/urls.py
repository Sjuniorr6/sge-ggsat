from django.urls import path
from . import views
from .views import download_pdf_requisicao, enviar_email_com_pdf, get_cliente_data



    #-------------------------------------------------------------------------------------------------------------

urlpatterns = [
    # Outras URLs
    path('requisicao/<int:id>/download/', download_pdf_requisicao, name='download_pdf_requisicao'),
    path('requisicao/<int:id>/enviar-email/', enviar_email_com_pdf, name='enviar_email_com_pdf'),
    path('requisicao/', views.RequisicoesViews.as_view(), name='requisicoes'),
    path('requisicaocreate', views.RequisicaoCreateView.as_view(), name='requisicoescrateview'),
    path('antenistaview', views.RegistrarEstoqueantenistaView.as_view(), name='RegistrarEstoqueantenistaView'),
    path('requisicoes/list', views.RequisicaoDetailView.as_view(), name='RequisicaoDetailView'),
    path('requisicao/requisicao/', views.RequisicaoUpdateView.as_view(), name='RequisicaoUpdateView'),
    path('requisicao/<int:pk>/update/', views.requisicoesdeleteview.as_view(), name='requisicoesdeleteview'),
#----------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
    path('tecnicoListView/', views.tecnicoListView.as_view(), name='tecnicoListView'),
    path('FinanceiroListViews/', views.FinanceiroListViews.as_view(), name='FinanceiroListViews'),
    path('tecnicoListView/<int:pk>/Update/', views.tecnicoUpdateView.as_view(), name='tecnicoUpdateView'),
    path('configlistview/', views.ConfiguracaoListView.as_view(), name='ConfiguracaoListView'),
    path('configuracao/<int:pk>/delete/', views.configuracaodeleteview.as_view(), name='ConfiguracaoListView'),
    path('config/list/<int:pk>/Update/', views.ConfiguracaoUpdateView.as_view(), name='ConfiguracaoUpdateView'),
    path('req/list/<int:pk>/Update/', views.Requisicao2UpdateView.as_view(), name='Requisicao2UpdateView'),
    path('config/list2/<int:pk>/Update/', views.ConfiguracaoUpdateView2.as_view(), name='ConfiguracaoUpdateView2'),
 #---------------------------------------------------------------------------------------------------------------
    path('ceo_list/list', views.ceoListViews.as_view(), name='ceoListViews'),  
      path('ceo_list/<int:pk>/detail/', views.ceodetailview.as_view(), name='ceodetailview'),
#--------------------------------------------------------------------------------------------------------------------   
      path('diretoria_list/', views.diretoriaListViews.as_view(), name='diretoriaListViews'),
#---------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------   
      path('expedicao_list/', views.expedicaoListViews.as_view(), name='expedicaoListViews'),
#---------------------------------------------------------------------------------------------------------------------
 path('historico_list/', views.historicoListView.as_view(), name='historicoListViews'),
#----------------------------------------------------------------------------------------------------------------------
    path('requisicao/diretoriaap/<int:id>/', views.aprovar_requisicao, name='aprovar_requisicao'),
    path('requisicao/diretoriaap/<int:id>/', views.reprovar_requisicao, name='reprovar_requisicao'),
  #--------------------------------------------------------------------------------------------------------------------- 
   #-----------------------------------------------------------------------------------------------------------------------------

    path('requisicao/reprovarrp/<int:id>/', views.Reprovar_diretoria, name='Reprovar_diretoria'),
    path('requisicao/aprovarrp/<int:id>/', views.Aprovar_diretoria, name='Aprovar_diretoria'),
#-----------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# 
 path('financeiro/ap/<int:id>/', views.aprovar_FINANCEIRO, name='APROVARFINANCEIRO'),
# 
# 
# ------------------------

     path('requisicao/aprovar/<int:id>/', views.aprovar_ceo, name='aprovar_ceo'),
    path('requisicao/reprovar/<int:id>/', views.reprovar_ceo, name='reprovar_ceo'),
#-------------------------------------------------------------------------------------------------------------  
  path('requisicao/expedir/<int:id>/', views.configurado_expedicao, name='configurado_expedicao'),
#---------------------------------------------------------------------------------------------------------------
path('requisicao/expedido/<int:id>/', views.expedicao_expedido, name='expedicao_expedido'),
path('manutencao/expedido/<int:id>/', views.expedicao_expedido2, name='expedicao_expedido2'),
path('expedir_requisicao/<int:id>/', views.expedir_requisicao, name='expedir_requisicao'),
path('expedir_requisicao_tec/<int:id>/', views.expedir_requisicaotec, name='expedir_requisicaotec'),
    path('expedir_manutencao/<int:id>/', views.expedir_manutencao, name='expedir_manutencao'),
     path('get-cliente-data/<int:cliente_id>/', get_cliente_data, name='get_cliente_data'),





]

path('manutencao/configurado/<int:id>/', views.configurado_manutencao, name='configurado_manutencao'),