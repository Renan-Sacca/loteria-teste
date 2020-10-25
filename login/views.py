from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import auth ,messages
from login.models import Profile
from login.models import Pessoa
from Home.models import fichas
import smtplib
import random
from rifas.models import rifa
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        sexo = request.POST['sexo']
        numero = request.POST['telefone']
        url = request.POST['urltrade']
        aniversario = request.POST['nasc']
        try:
            fotos = request.FILES['foto']
        except :
            fotos = 'Looteria/static/imagens/user.png'

        

        
        if not username.strip():
            print('O campo Username não pode ficar em branco')
            messages.error(request, 'O campo Username não pode ficar em branco')
            
            return redirect('cadastro')
        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not sobrenome.strip():
            messages.error(request, 'O campo sobrenome não pode ficar em branco')
            print('O campo sobrenome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            messages.error(request, 'Email já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=username).exists():
            print('Usuário já cadastrado')
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')



        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("looterya@gmail.com", "nwvrsuygdxnkihcr")
        msgFrom = str(email)
        cod = random.randrange(100000,999999)
        msg = "Numero de ativacao da sua conta e {}".format(cod)
        print(msg)
        msgTo = 'looterya@gmail.com'
        assunto = "Confirmacao de email"
        server.sendmail(msgTo,msgFrom,'Subject: {}\n{}'.format(assunto,msg))

        server.quit()
        
        user = User.objects.create_user(username=username, email=email, password=senha,first_name=nome, last_name =sobrenome)  
        user.save() 
        user = auth.authenticate(request, username=username, password=senha)
        auth.login(request, user)

        profile = Profile.objects.create(numero=numero,sexo=sexo,cod_conf=cod,ativado=False,user_id = request.user.id,pontos=0,urltrade=url,aniversario=aniversario,foto=fotos)     
        profile.save()
        print('Usuário cadastrado com sucesso')

        pessoa = Pessoa.objects.create(nome=nome,email=email,username=username,telefone=numero,senha=senha)
        pessoa.save()

        
        return redirect('dashboard')
    else:
        return render(request,'registrar.html')
    return render(request,'registrar.html')

def login(request):
    if request.method == 'POST':
        usuario =  request.POST['usuario']
        senha = request.POST["senha"]
        if usuario == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            print(usuario, senha)
            return render(request,'login.html')
        if User.objects.filter(email=usuario).exists():
            nome = User.objects.filter(email=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            print(nome)
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            print('Login realizado com sucesso')
            
            return redirect('dashboard')

        return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    
    rifas = rifa.objects.all()
    dados={
        'rifa' : rifas,
    }
    print(dados)
    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return redirect('index')
    
def perfil(request):
    profiles = Profile.objects.get(user=request.user.id)
    
    dados={
        'profiles' : profiles,
    }
    return render(request,'perfil.html',dados)

def alterarsenha(request):
    if request.method == 'POST':
        print("teste")
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            print("entrou")
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "Perfil.html")
        else:
            print("não entrou")
            return redirect("index")
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form':form,
        }
        return render(request, "alterarsenha.html",context)

def alterardado(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        url = request.POST['url']
        telefone = request.POST['telefone']
        print(nome,sobrenome,email,url,telefone)
        profiles = Profile.objects.get(user=request.user.id)

        profiles.urltrade = url
        profiles.numero = telefone
        profiles.save()

        request.user.first_name = nome
        request.user.last_name = sobrenome
        request.user.email = email

        request.user.save()


        


    return redirect('perfil')

def ativar(request):
    return render(request,'ativarConta.html')

def esquecisenha(request):
    return render(request,'esquecisenha.html')

    
def resetsenha(request):
    return render(request,'esquecisenha.html')


