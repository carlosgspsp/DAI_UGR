# recetas/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import *
from .models import *

# Create your views here.

def recetas(request):
    if request.POST.get('receta'):
        recetasListadas = Receta.objects.filter(nombre=request.POST.get('receta'))
    else:
        recetasListadas = Receta.objects.all

    return render(request,'recetas.html',{'recetasListadas' : recetasListadas})


def ver_receta(request,pk):
    receta = Receta.objects.get(id=pk)
    ingredientes = Ingrediente.objects.filter(receta = pk)
    fotos = Foto.objects.filter(receta = pk)
    return render(request,'ver_receta.html',{'receta' : receta, 'ingredientes':ingredientes, 'fotos':fotos})

@login_required
def crear_receta(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form = RecetasForm(request.POST)
            if form.is_valid() :
                receta = form.save(commit=False)
                receta.save()
                messages.success(request, F"La receta ha sido creada con éxito")
                return redirect('/')
            else:
                messages.error(request, F"Fallo")
        else:
            form = RecetasForm()
        titulo = "Crear receta"
        return render(request,'crear_editar_receta.html',{'form':form,'titulo':titulo})
    else:
        messages.warning(request, "No tienes permisos para crear una receta")
        return redirect('/')


#-- En caso de querer pedir el login antes de acceder
@login_required
def editar_receta(request,pk):
    if request.user.is_authenticated and request.user.is_staff:
        receta = Receta.objects.get(id=pk)
        fotos = Foto.objects.filter(receta=pk)


        form = RecetasForm(instance=receta)
        form2 = FotoForm()

        if request.method == "POST":
            if request.POST.get('recetaform'):
                form = RecetasForm(request.POST, instance=receta)
                if form.is_valid():
                    form.save()
                    messages.success(request, F"La receta ha sido actualizado!")
                    return redirect('/')
                else:
                    messages.error(request, F"Formulario de receta no válido")
            elif request.POST.get('fotoform'):
                form2 = FotoForm(request.POST, request.FILES)
                if form2.is_valid():
                    #form2.receta = pk
                    form2.save()
                    messages.success(request, F"La foto ha sido actualizado!")
                    return redirect('/')
                else:
                    messages.error(request, F"Formulario de receta no válido")
            else:
                messages.error(request, F"Sin formulario")

        edito = True
        titulo = "Editar receta"
        return render(request,'crear_editar_receta.html',{'form':form,'fotos':fotos,'titulo':titulo,'form2':form2,'edito':edito,'receta':receta})
    else:
        messages.warning(request, "No tienes permisos")
        return redirect('/')
@login_required
def borrar_receta(request,pk):
    if request.user.is_authenticated and request.user.is_superuser:
        receta = Receta.objects.get(id=pk)
        receta.delete()
        messages.success(request, F"La receta {receta.nombre} ha sido eliminada")
        return redirect('/')
    else:
        messages.warning(request, "No tienes permisos suficientes para borrar la receta")
        return redirect('/')

def register(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, F"Se ha creado al usuario {username}")
        else:
            form = UserRegisterForm    
        return render(request, "registration/register.html",{'form':form})
    else:
        messages.warning(request, "No tienes permisos")
        return redirect('/')

def usuarios(request):
    usuarios = User.objects.all
    return render(request,'usuarios.html',{'usuarios':usuarios,})


def borrar_usuario(request,pk):
    if request.user.is_authenticated and request.user.is_staff:
        usuario = User.objects.get(id=pk)
        usuario.delete()
        messages.success(request, F"El usuario {usuario.username} ha sido eliminado")
        return redirect('/usuarios')
    else:
        messages.warning(request, "No tienes permisos")
        return redirect('/')


@login_required
def borrar_foto(request,pk):
    if request.user.is_authenticated and request.user.is_staff:
        archivo = Foto.objects.get(id=pk)
        Receta = archivo.receta
        archivo.delete()
        messages.success(request, F"El archivo ha sido eliminado!")
        return redirect('/editar_receta/'+str(Receta.id))
    else:
        messages.warning(request, "No tienes permisos")
        return redirect('/')