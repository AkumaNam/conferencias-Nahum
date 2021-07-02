from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('', views.index, name='index'),
    path('participantes/', views.participantes, name="participantes"),
    path('participantes/<int:id>/eliminar/', views.eliminar_participantes, name='eliminar_participante'),
    path('participantes/<int:id>/editar/', views.editar_participantes, name='editar_participante'),
    path('conferencias/', views.conferencias, name='conferencias'),
    path('asistir/<int:id>/conferencias/<str:accion>/', views.asistir, name='asistir'),
]
