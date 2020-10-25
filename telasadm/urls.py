from django.urls import path

from . import views

urlpatterns = [
    path('', views.cd_skin, name='cd_skin'),
    path('rifa/', views.cd_rifa, name='cd_rifa'),
    path('sorteio/', views.sorteio, name='sorteio'),
    path('<int:id>sortear/', views.sortear, name='sortear'),
]