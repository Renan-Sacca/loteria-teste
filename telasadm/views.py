from django.shortcuts import render,redirect
from rifas.models import skin
from rifas.models import rifa
import random
from datetime import date
import json
def cd_skin(request):
    if request.method == 'POST':
        categoria =  request.POST['categoria']
        nome =  request.POST['nome']
        valor =  request.POST['valor']
        link =  request.POST['link']
        skins = skin.objects.create(nome=nome,categoria=categoria,valor=valor,link=link)     
        skins.save()
        return render(request,'cd_skin.html')

    return render(request,'cd_skin.html')
def sorteio(request):
    rifas = rifa.objects.filter(ativa=True)
    dados={
        'rifa' : rifas,
    }
    return render(request,'sorteio.html', dados)

def sortear(request,id):
    rifas = rifa.objects.get(id=id)
    
    dados_rifa = json.loads(rifas.participantes)
    dados_ganhador = json.loads(rifas.ganhador)

    ta = len(dados_rifa)
    num = random.randint(1, ta)
    sorteio = True
    data_atual = date.today()
    while sorteio:
        if dados_rifa[str(num)]["nome"] == "":
            num = random.randint(1, ta)
            
        else:
            dados_ganhador["nome"]=dados_rifa[str(num)]["nome"]
            dados_ganhador["foto"]=rifas.skin.link
            dados_ganhador["skinn"]=rifas.skin.nome
            dados_ganhador["data"]= '{}/{}/{}'.format(data_atual.day, data_atual.month,
data_atual.year)
            sorteio = False
    print(dados_ganhador)
    rifas.ganhador = json.dumps(dados_ganhador)

    rifas.ativa = False
    rifas.e_ganhador = True
    rifas.save()

    rifas = rifa.objects.filter(ativa=True)
    dados={
        'rifa' : rifas,
    }
    return render(request,'sorteio.html', dados)

def cd_rifa(request):
    if request.method == 'POST':
        valor_total =  request.POST['valor_total']
        num_entradas =  request.POST['num_entradas']
        valor_entrada =  request.POST['valor_entrada']
        
        data_inicial =  request.POST['data_inicial']
        data_final =  request.POST['data_final']
        id_skin =  request.POST['id_skin']
        ativa =  request.POST['ativa']
        skins = skin.objects.get(id=int(id_skin))
        participantes = "{"
        for i in range(1,int(num_entradas)+1):
            participantes += '"' + str(i) + '":{"numero":' + '"'+ str(i) + '","nome":"","foto":""},'

        participantes = participantes[0:-1]
        participantes += "}"  
        
        ganhador = '{"nome":"","data":"","skinn":"","foto":""}' 

        rifas = rifa.objects.create(valor_total=valor_total,num_entradas=num_entradas,valor_entrada=valor_entrada,participantes=participantes,data_inicial=data_inicial,data_final=data_final,skin=skins,ativa=ativa,num_part=0,premium=True,ganhador=ganhador,e_ganhador=False)     
        rifas.save()
        return render(request,'cd_rifa.html')




    return render(request,'cd_rifa.html')


