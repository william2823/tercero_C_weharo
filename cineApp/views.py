from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import peliculas
from django.contrib import messages

def inscribirse(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'inscribrise.html ', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'inscribrise.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def iniciarsesion(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/perfil')  # profile
        else:
            msg = 'Usuario o contraseña incorrecta'
            form = AuthenticationForm(request.POST)
            return render(request, 'acceso.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'acceso.html', {'form': form})


def perfil(request):
    return render(request, 'perfil.html')


def salir(request):
    logout(request)
    return redirect('/')
#######################

def homedef(request):
    cursosListados = peliculas.objects.all()
    messages.success(request, 'Pelicula Ingresadas')
    return render(request, "gestioncine.html", {"cursos": cursosListados})


def registrarcine(request):
    codigo = request.POST['Codigo']
    titulo = request.POST['titulo']
    precios = request.POST['numprecios']

    curso = peliculas.objects.create(
        codigo=codigo, titulo=titulo, precios=precios)
    messages.success(request, '¡Registrado!')
    return redirect('/')


def edicioncine(request, codigo):
    curso = peliculas.objects.get(codigo=codigo)
    return render(request, "edicioncine.html", {"curso": curso})


def editarcine(request):
    codigo = request.POST['Codigo']
    titulo = request.POST['titulo']
    precios = request.POST['numprecios']

    curso = peliculas.objects.get(codigo=codigo)
    curso.titulo = titulo
    curso.precios = precios
    peliculas.save()

    messages.success(request, 'Pelicula actualizada')

    return redirect('/')


def eliminarcine(request, codigo):
    curso = peliculas.objects.get(codigo=codigo)
    peliculas.delete()

    messages.success(request, 'Pelicula eliminada')

    return redirect('/')