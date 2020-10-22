from django.shortcuts import render,redirect
from rifas.models import rifa
from rifas.models import skin
from django.contrib.auth.models import User
from django.contrib import auth
from login.models import Profile

def pagamentos(request):
    if request.user.is_authenticated:
        print(User)
        return render(request,'pagamentos.html')

    rifas = rifa.objects.all()
    skins = skin.objects.all()
    dados={
        'rifa' : rifas,
        'skin' : skins,
    }
   
    return render(request,'index.html', dados)



    
    
def formas_pag(request,valor):
    dados = {
        'valor' : valor,
    }
    return render(request,'formas_pag.html',dados)

