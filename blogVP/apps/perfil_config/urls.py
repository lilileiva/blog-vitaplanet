from django.urls import path
from . import views

app_name = 'perfil_config'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Perfil_config, name = 'perfil_config'),

]
