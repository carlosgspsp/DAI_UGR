# recetas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recetas, name='recetas'),
    path('ver_receta/<int:pk>', views.ver_receta, name='ver_receta'),
    path('crear_receta/', views.crear_receta, name='crear_receta'),
    path('editar_receta/<int:pk>', views.editar_receta, name='editar_receta'),
    path('borrar_receta/<int:pk>', views.borrar_receta, name='borrar_receta'),
    path('register/', views.register, name='register'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('borrar_usuario/<int:pk>', views.borrar_usuario, name='borrar_usuario'),

    path('borrar_foto/<int:pk>', views.borrar_foto, name='borrar_foto'),
]