from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
            return redirect(reverse('registro:index'))
    return render(request, 'seguridad/index.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password)

        print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('registro:index'))
            else:
                return HttpResponse('El usuario existe pero no esta activo')

        else:
            messages.add_message(request, messages.ERROR, ' El usuario/contraseña invaidos o la cuenta esta desactivada')
            return redirect('/')

        return HttpResponse(f'Usuario: {user} - Clave : {password}')
    else:
        return redirect('/')

def log_out(request):
    logout(request)
    return redirect('/')