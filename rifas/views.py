from django.shortcuts import render,redirect
from rifas.models import rifa
from login.models import Profile
from django.contrib.auth.models import User
from django.contrib import auth,messages
from rifas.models import rifa
import json
from rifas.models import skin


def historico(request):  
    rifas = rifa.objects.filter(e_ganhador=True)
    dados_json = []
    for rifaa in rifas:
        dados_json.append(json.loads(rifaa.ganhador))


    print(dados_json)
    dados={
        'rifa' : dados_json,
    }
    return render(request,'historico.html', dados)

def Rifas(request,valor):

    rifas = rifa.objects.filter(id=valor)
    profiles = Profile.objects.filter(user=request.user.id)
    for rifaa in rifas:
        dados_json = rifaa.participantes
    
    dados_json = json.loads(dados_json)
    t = [0] * len(dados_json)

    for teste in dados_json:
        t[int(teste)-int(1)] = dados_json[teste]
        

    
    
    
    dados = {
        'rifa' : rifas,
        'profile': profiles,
        'particante':dados_json,
        't':t,
        'valor':valor,
    }
    
    return render(request,'rifas.html',dados)

def rifas_p(request):    
    rifas = rifa.objects.filter(ativa=True)
    #rifas2 = rifa.objects.filter(ativa=True).order_by('skin_id','categoria')
    #print(rifas2)
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


    
def comprarrifa(request,valor,id):
    profiles = Profile.objects.get(user=request.user.id)
    rifas = rifa.objects.get(id=valor)
    
    if profiles.pontos < rifas.valor_entrada:
        print("se n tem grana")
        messages.error(request, 'Pobre')
        return redirect("Rifas",valor)

    dados_json = json.loads(rifas.participantes)
    
    dados_json[str(id)]["nome"] = request.user.username
    dados_json[str(id)]["foto"] = profiles.foto.url
    profiles.pontos -= rifas.valor_entrada
    profiles.save()
    rifas.participantes = json.dumps(dados_json)
    rifas.num_part +=1
    rifas.save()
    print(dados_json)
    
    return redirect("Rifas",valor)

    