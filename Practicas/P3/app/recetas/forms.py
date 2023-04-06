from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class RecetasForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre', 'preparación')
        labels = {
            'nombre' : 'Nombre',
            'preparación' : 'Preparación',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'nombre de la receta'}),
            'preparación' : forms.Textarea(attrs={'class':'form-control', 'rows':'3','placeholder' : 'Preparación de la receta'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasefa', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contrasenia', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_staff','is_superuser']


class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('foto','receta')
        widgets = {
            'foto' : forms.FileInput(attrs={'class':'custom-file-input'}),
            'receta' : forms.Select(attrs={'class':'form-control'}),
        }
