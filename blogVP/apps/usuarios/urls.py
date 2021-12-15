from django.urls import path
from . import views
from apps.usuarios.views import Registro

app_name = 'registro'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', Registro.as_view(), name = 'registro'),

]