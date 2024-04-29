from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('create', views.add_inventary, name='create'),
    path('reload', views.reload, name='reload'),
    path('login', views.login,name='login'),
    path("register", views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('edit/<str:id>', views.edit, name='edit'),
    #path('test', views.test, name = 'test'),
    path('get-info', views.get_info, name='get-info'),
    path('notifications', views.notificaciones, name='notifications'),
    path('action', views.accion_notificacion, name='action'),
    path('asignar', views.asignacion, name='asignacion'),
    path('asignaciones', views.asignaciones, name='asignaciones'),
    path('importar', views.importar_datos, name = "importar"),
    path("informes", views.importar_datos, name="informes"),
    path("administrar_usuario", views.administrar_users, name="admin_users"),
    path("to_admin", views.to_admin, name="to_admin"),
    path("to_active", views.to_active, name="to_active"),
    path('cambio-contraseña', views.cambio_contraseña, name='cambio_contraseña')
]