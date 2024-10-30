from django.urls import path
from .views import paradaCreateView, paradaListView,get_choices,passagemCreateView,PassagemListView,get_pa_choices
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pparada/', paradaCreateView.as_view(), name='paradaseguraform'),
    path('pa_list/', paradaListView.as_view(), name='paradaseguralist'),
    path('get-choices/', get_choices, name='get_choices'),
    path('passagem/', passagemCreateView.as_view(), name='passagemCreateView'),
    path('historico/', PassagemListView.as_view(), name='historico_passagem'),
    path('get_pa_choices/', get_pa_choices, name='get_pa_choices'),
    
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)