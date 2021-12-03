from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Registro, name = 'registro'),

]
