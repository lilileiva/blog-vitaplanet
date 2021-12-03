from django.urls import path
from . import views

app_name = 'ingreso'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Ingreso, name = 'ingreso'),

]