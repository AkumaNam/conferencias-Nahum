"""conferencias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_registro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #si es pequeño todo aqui sino la 3 opcion de arriva
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('participantes/', views.participantes, name="participantes"),
    path('participantes/<int:id>/eliminar/', views.eliminar_participantes, name='eliminar_participante'),
    path('participantes/<int:id>/editar/', views.editar_participantes, name='editar_participante'),
    path('conferencias/', views.conferencias, name='conferencias')
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('_debug_/', include(debug_toolbar.urls)),
