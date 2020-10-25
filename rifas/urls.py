from django.urls import path

from . import views

urlpatterns = [
    path('<int:valor>', views.Rifas, name='Rifas'),
    path('rifas_premium', views.rifas_p, name='rifas_p'),
    path('rifas_free', views.rifas_f, name='rifas_f'),
    path('<int:valor>/<int:id>', views.comprarrifa, name='comprarrifa'),
    path('historico',views.historico, name='historico'),


]