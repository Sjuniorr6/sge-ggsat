from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', include('login.urls')),       
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),          
    path('produto/', include('produto.urls')),    
    path('cliente/', include('cliente.urls')),    
    path('acompanhamento/', include('acompanhamento.urls')),  
    path('tuper/', include('tuper.urls')),        
    path('usuarios/', include('usuarios.urls')),        
    path('estoque/', include('estoque.urls')),        
    path('saidas/', include('saidas.urls')),        
    path('reativacao/', include('reativacao.urls')),        
    path('manutencaolist/', include('manutencaolist.urls')),        
          
    path('formulariov/', include('formulariov.urls')),        
    path('formularioe/', include('formularioe.urls')),        
    path('faturamento/', include('faturamento.urls')),  
    path('register/', include('register.urls')),  
    path('requisicao/', include('requisicao.urls')),  
    path('registrodemanutencao/', include('registrodemanutencao.urls')),  
    path('formacompanhamento/', include('formacompanhamento.urls')),  
    path('prestadores/', include('prestadores.urls')),  
    path('regcliente/', include('regcliente.urls')),  
    path('qualit/', include('qualit.urls')),  
    path('dashboard/', include('dashboard.urls')),  
    path('adm/', include('adm.urls')),  
    path('iao_list/', include('IAO.urls')),
    path('pparada/', include('pparada.urls')),

    path('ticket/', include('ticket.urls')),
    path('t42/', include('t42.urls')),

   

   
     
     
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)