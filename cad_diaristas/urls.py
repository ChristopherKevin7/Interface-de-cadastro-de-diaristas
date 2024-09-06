from django.urls import path
from app_cad_diarista import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #Rota, view responsável, nomede referência
    path('',views.home, name='home'),
    path('cadempresas/', views.home_empresa, name='home_empresa'),
    path('diaristas/', views.diaristas, name= 'listagem_diaristas'),
    path('editar/<int:id_diarista>/', views.editar, name= 'editar'),
    path('editarempresa/<int:id_empresa>/', views.editar_empresa, name= 'editar_empresa'),
    path('update/<int:id_diarista>/', views.update, name= 'update'),
    path('updateempresa/<int:id_empresa>/', views.update_empresa, name= 'update_empresa'),
    path('excluir/<int:id_diarista>/', views.excluir_item, name= 'excluir_item'),
    path('excluirempresa/<int:id_empresa>/', views.excluir_item_empresa, name= 'excluir_item_empresa'),
    path('empresas/', views.empresas, name='listagem_empresas'),
    path('read/', views.read, name='read'),
    path('readempresa/', views.read_empresa, name='read_empresa'),
    path('recibo/<int:id_diarista>/', views.recibo, name='recibo'),
    path('emitir/<int:id_diarista>/<int:id_empresa>/', views.emitir_recibo, name='emitir_recibo')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 