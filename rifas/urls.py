from django.urls import path

from . import views

urlpatterns = [
    path('<int:valor>', views.rifas, name='rifas'),
    path('rifas_premium', views.rifas_p, name='rifas_p'),
    path('rifas_free', views.rifas_f, name='rifas_f'),


]