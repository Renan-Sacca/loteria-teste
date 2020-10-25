from django.shortcuts import render,redirect
from rifas.models import rifa
from login.models import Profile
from django.contrib.auth.models import User
from django.contrib import auth
from rifas.models import rifa
import json
from rifas.models import skin



def rifas(request,valor):
    rifas = rifa.objects.filter(id=valor)
    profiles = Profile.objects.filter(user=request.user.id)
    for rifaa in rifas:
        dados_json = rifaa.participantes
    
    
    dados_json = json.loads(dados_json)
    t = [0] * len(dados_json)
    for teste in dados_json:
        t[int(teste)-int(1)] = dados_json[teste]
        
    print(t)
    
    deda = [{"nome":"renan","foto":"dwa"},{"nome":"beta","foto":"blabla"}] 
    print(deda) 
    
    dados = {
        'rifa' : rifas,
        'profile': profiles,
        'particante':dados_json,
        'teste':deda,
        't':t,
    }
    
    return render(request,'rifas.html',dados)

def rifas_p(request):    
    rifas = rifa.objects.all()
    dados={
        'rifa' : rifas,
    }
    return render(request,'rifa_p.html', dados)

def rifas_f(request):    
    rifas = rifa.objects.all()
    dados={
        'rifa' : rifas,
    }
    return render(request,'rifa_f.html', dados)
    