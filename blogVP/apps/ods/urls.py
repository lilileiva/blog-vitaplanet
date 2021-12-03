from django.urls import path
from . import views

app_name = 'ods'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.Ods, name = 'ods'),

]