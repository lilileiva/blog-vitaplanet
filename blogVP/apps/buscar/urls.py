from django.urls import path
from . import views

app_name = 'buscar'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Buscar, name = 'buscar'),

]