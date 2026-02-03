from django.urls import path
from . import views

urlpatterns = [
    # URLs para Roles
    path('roles/', views.lista_roles, name='lista_roles'),
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/<int:rol_id>/editar/', views.editar_rol, name='editar_rol'),
    path('roles/<int:rol_id>/eliminar/', views.eliminar_rol, name='eliminar_rol'),
    
    # URLs para Permisos
    path('permisos/', views.lista_permisos, name='lista_permisos'),
    path('permisos/crear/', views.crear_permiso, name='crear_permiso'),
    path('permisos/<int:permiso_id>/editar/', views.editar_permiso, name='editar_permiso'),
    path('permisos/<int:permiso_id>/eliminar/', views.eliminar_permiso, name='eliminar_permiso'),
]