from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not username or not email or not senha:
            messages.add_message(request, messages.ERROR, "Todos os campos devem ser preenchidos.")
            return redirect('cadastro')

        user = User.objects.filter(email=email).exists()

        if user:
            messages.add_message(request, messages.ERROR, "E-mail já cadastrado.")
            return redirect('cadastro')
        
        user = User.objects.filter(username=username).exists()

        if user:
            messages.add_message(request, messages.ERROR, "Nome de usuário já cadastrado.")
            return redirect('cadastro')

        User.objects.create_user(
            username=username,
            email=email,
            password=senha,
            first_name=username
        )

        messages.success(request, 'Conta criada com sucesso!')
        return redirect('login')
    return render(request, 'cadastro.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'E-mail ou senha incorretos.')
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='login')
def comunidade(request):
    busca = request.GET.get('q')

    posts = Post.objects.all()

    if busca:
        posts = posts.filter(
            titulo__icontains=busca
        )

    return render(request, 'comunidade.html', {
        'posts': posts
    })
    # posts = Post.objects.all()
    # return render(request, 'comunidade.html', {'posts': posts})

@login_required(login_url='login')
def criar_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        categoria = request.POST.get('categoria')
        conteudo = request.POST.get('texto')

        if not titulo or not categoria or not conteudo:
            messages.add_message(request, messages.ERROR, "Preencha todos os campos para criar um post.")
            return redirect('criar_post')
        
        Post.objects.create(
            titulo = titulo,
            categoria = categoria,
            texto = conteudo,
            autor = request.user
        )

        messages.success(
            request,
            "Post criado com sucesso!"
        )

        return redirect('comunidade')
    return render(request, 'criar_post.html')

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def detalhe_post(request, id):
    post = get_object_or_404(Post, id=id)

    return render(request, 'detalhe_post.html', {
        'post': post
    })