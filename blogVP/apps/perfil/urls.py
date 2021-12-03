from django.urls import path
from . import views

app_name = 'perfil'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Perfil, name = 'perfil'),

]