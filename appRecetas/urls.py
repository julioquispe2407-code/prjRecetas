from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('nueva/', views.nueva_receta, name='nueva_receta'),
    path('create-superuser-temp/', views.create_superuser_temp, name='create_superuser_temp'),
]