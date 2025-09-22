from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_recetas, name='lista_recetas'),
    path('<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('nueva/', views.nueva_receta, name='nueva_receta'),
    path('run-migrations/', views.run_migrations, name='run_migrations'),
]