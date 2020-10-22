from django.urls import path

from . import views

urlpatterns = [
    path('pagamento', views.pagamentos, name='pagamentos'),
    path('<int:valor>', views.formas_pag, name='formas_pag'),


]