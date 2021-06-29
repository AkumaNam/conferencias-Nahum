from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'seguridad/index.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('contrasena')

        user = authenticate(username=username, password=password)

        if user is not None:
            return HttpResponse('El usuario existe')
        else:
            return HttpResponse('El usuario no existe')

        return HttpResponse(f'Usuario: {user} - Clave : {password}')
