from django.urls import path
from . import views
from apps.usuarios.views import Registro, RegistroForm

app_name = 'usuarios'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('registro/', Registro.as_view(), name = 'registro'),

]