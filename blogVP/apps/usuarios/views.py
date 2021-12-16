from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from apps.usuarios.models import Usuario
from apps.usuarios.forms import RegistroForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import *
from . import views


class Registro(CreateView):
    model = Usuario
    template_name = "usuarios/registro.html"
    form_class = RegistroForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario_log = authenticate(username=usuario, password=password)
        login(self.request, usuario_log)
        return redirect('principal')