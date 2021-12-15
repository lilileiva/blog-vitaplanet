from django.shortcuts import render
from apps.usuarios.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.usuarios.forms import RegistroForm

class Registro(CreateView):
	model = Usuario
	template_name = "usuarios/registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('principal')