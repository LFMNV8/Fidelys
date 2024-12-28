from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
import random
import string
from .models import *



def home(request):
    return render(request, 'home.html')
    

def planoseservico(request):
    return render(request, 'planoseprecos.html')

def carregamento1(request):
    return render(request, 'carregamento1.html')

def carregamentologadoplanos(request):
    return render(request, 'carregamentologadoplanos.html')

def carregamentologadoplanospage(request):
    return render(request, 'planoseprecoslogado.html')

def carregamentohome(request):
    return render(request, 'carregamentohome.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login_view(request):  
    return render(request, 'login.html')

def carregamentocadastro(request):
    return render(request, 'carregamentocadastro.html')

def carregamentologin(request):
    return render(request,'carregamentologin.html')



def criar_usuario(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento') 
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, "As senhas não coincidem.")
            return render(request, 'cadastro.html')

        primeiro_nome = nome.split(' ')[0]

        username = primeiro_nome
        i = 1
        while User.objects.filter(username=username).exists():
            username = f"{primeiro_nome}{i}"
            i += 1

        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já Cadastrado!")
            return render(request, 'cadastro.html')
        
        if UserProfile.objects.filter(cpf=cpf).exists():
            messages.error(request, "Cpf já Cadastrado!")
            return render(request, 'cadastro.html')

        
        try:
            user = User.objects.create_user(
                username=username,
                first_name=nome,
                email=email,
                password=senha
            )

            profile = UserProfile.objects.create(
                user=user,
                cpf=cpf,
                data_nascimento=data_nascimento
            )

            messages.success(request, "Usuário criado com sucesso!")
            return redirect('login')

        except Exception as e:
            messages.error(request, "Erro ao criar o usuário. Tente novamente.")
            return render(request, 'cadastro.html')

    return render(request, 'cadastro.html')




def login_usuario(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            user = authenticate(request, username=user.username, password=senha)

        if user is not None:
            login(request, user)
            messages.success(request, "Login bem-sucedido!")
            return redirect('home_logado')  
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")
            return render(request, 'login.html')
    
    return render(request, 'login.html')

@login_required
def atualizar_imagem(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            profile.image = form.cleaned_data['image']
            profile.save()
            return redirect('home_logado')  
        form = UserProfileForm()

    return render(request, 'home.html', {'form': form})

@login_required
def home_logado(request):
    return render(request, 'home_logado.html')

@login_required
def carregamentohomelogado(request):
    return render(request, 'carregamentohomelogado.html')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_new_password')
        current_password = request.POST.get('current_password')  

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, "Senha atual incorreta.")
        

        if new_password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
        
        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, "Senha alterada com sucesso. Bem-vindo de volta!")
    

    return render(request, 'login.html')


def generate_random_password(length=8):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                new_password = generate_random_password()
                user.set_password(new_password)
                user.save()

                email_subject = 'Nova Senha'
                email_body = f'Olá {user.first_name},\n\nSua nova senha é: {new_password}\n\nPor favor, use essa senha para acessar sua conta.'
                
                send_mail(
                    email_subject,
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'Sua nova senha foi enviada para seu e-mail.')

            except User.DoesNotExist:
                messages.error(request, 'Nenhum usuário encontrado com este e-mail!')

            except Exception as e:
                messages.error(request, f'Erro ao enviar o e-mail! Tente novamente. Detalhes: {str(e)}')

        else:
            messages.error(request, 'Nenhum e-mail foi fornecido.')

        return render(request, 'login.html')

    return render(request, 'core/login.html')