from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagamentos, name='pagamentos'),
    path('<int:valor>', views.formas_pag, name='formas_pag'),
    path('pagado/<int:valor>', views.pagou, name='pagou'),


]