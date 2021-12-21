from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostCommentView,
    like,
    Busqueda,
    Filtrar
    )
from . import views

app_name='Post'

urlpatterns = [
    path('list/', PostListView.as_view(), name ='list'),
    path('create/', PostCreateView.as_view(), name ='create'),
    path('<int:pk>/', PostDetailView.as_view(), name ='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name ='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name ='delete'),
    path('like/<int:pk>/', like, name='like'),
    path('<int:pk>/comment/', PostCommentView.as_view(), name = 'comment'),
    path('buscar/', views.Busqueda, name="buscar"),
    path('filtrar/', views.Filtrar, name="filtrar")
]