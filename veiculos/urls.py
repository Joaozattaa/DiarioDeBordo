from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_veiculos, name='lista_veiculos'),
    path('qr_code/<int:veiculo_id>/', views.gerar_qr_code, name='gerar_qr_code'),
    path('veiculo/<int:veiculo_id>/', views.registrar_uso, name='registrar_uso'),
    path('sucesso/<int:veiculo_id>/', views.sucesso, name='sucesso'),

]
