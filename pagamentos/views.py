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
    profiles = Profile.objects.filter(user=request.user.id)
    dados = {
        'valor' : valor,
        'profile': profiles,
    }
    return render(request,'formas_pag.html',dados)

def pagou(request,valor):
    profiles = Profile.objects.get(user=request.user.id)
    if valor == 2:
        profiles.pontos += 200
    elif valor == 5:
        profiles.pontos += 500
    elif valor == 10:
        profiles.pontos += 1000
    elif valor == 20:
        profiles.pontos += 2100
    elif valor == 50:
        profiles.pontos += 5400
    elif valor == 99:
        profiles.pontos += 11000

    profiles.save()
    return redirect('index')
    