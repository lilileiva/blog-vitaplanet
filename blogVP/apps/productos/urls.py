from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Productos, name = 'productos'),

]