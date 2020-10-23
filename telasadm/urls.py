from django.urls import path

from . import views

urlpatterns = [
    path('', views.cd_skin, name='cd_skin'),
    path('rifa/', views.cd_rifa, name='cd_rifa'),
]