from django.urls import path

from . import views

urlpatterns = [
    path('<int:valor>', views.rifas, name='rifas'),


]