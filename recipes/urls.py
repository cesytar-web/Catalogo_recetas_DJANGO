from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_recetas, name='listar_recetas'),
    path('receta/<int:receta_id>/', views.ver_receta, name='ver_receta'),
    path('crear/', views.crear_receta, name='crear_receta'),
    path('eliminar/<int:receta_id>/', views.eliminar_receta, name='eliminar_receta'),  # Nueva ruta para eliminar receta
]

