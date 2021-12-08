"""blogVP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.Principal, name = 'principal'),

    path('inicio/', include('apps.inicio.urls')),

    path('registro/', include('apps.registro.urls')),

    path('ods/', include('apps.ods.urls')),

    path('perfil/', include('apps.perfil.urls')),

    path('perfil_config/', include('apps.perfil_config.urls')),

    path('buscar/', include('apps.buscar.urls')),

    path('ingreso/', include('apps.ingreso.urls')),

    path('login/', auth.LoginView.as_view(template_name="usuarios/login.html"), name = 'login'),
    path('logout/', auth.LoginView.as_view(template_name="usuarios/logout.html"), name = 'logout'),

    path('productos/', include('apps.productos.urls'))
]
