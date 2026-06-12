

from django.contrib import admin
from django.urls import path
from afiliados.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # default
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('afiliados/', afiliados, name='afiliados'),
    path('perfil/', settings, name='settings'),
    path('afiliados/data/', afiliados_data, name='afiliados_data'),
    path("cargar_excel/", cargar_afiliados_excel, name="cargar_excel"),
    path("afiliado/<int:afiliado_id>/editar/", editar_afiliado, name="editar_afiliado"),
    path("crear_afiliado/", crear_afiliado, name="crear_afiliado"),
    path("atenciones/", atenciones_view, name="atenciones"),
    path("atenciones/list/<int:afiliado_id>/", atenciones_list, name="atenciones_list"),
    path("afiliados/search/", afiliados_search, name="afiliados_search"),
    path("afiliado/<int:afiliado_id>/info/", get_afiliado_info, name="get_afiliado_info"),
    path('atenciones/data/', atenciones_data, name='atenciones_data'),
    path("atenciones/create/", atenciones_create, name="atenciones_create"),
    path("admin-panel/", admin_panel, name="admin_panel"),
    path('users/search/', admin_users_search, name='admin_users_search'),
    path('change-password/', admin_change_password, name='admin_change_password'),
    path('settings/change-password/', change_own_password, name='change_own_password'),
    path('settings/change-email/', change_own_email, name='change_own_email'),
    path("create-users-excel/", create_users_from_excel, name="create_users_excel"),
    path('admin-panel/users/data/', admin_users_list_data, name='admin_users_list_data'),
    path('admin-panel/users/create/', crear_usuario_manual, name='crear_usuario_manual'),
    path('admin-panel/users/toggle/<int:user_id>/', toggle_user_status, name='toggle_user_status'),
    path('admin-panel/users/template/', descargar_plantilla_usuarios, name='descargar_plantilla_usuarios'),
    path('admin-panel/users/upload/', cargar_usuarios_excel_ajax, name='cargar_usuarios_excel_ajax'),
    path('afiliados/<int:afiliado_id>/marcar-servicio/', marcar_servicio_cumplido, name='marcar_servicio_cumplido'),
    path('reportes/', reportes_view, name='reportes'),
    path('afiliados/<int:afiliado_id>/eliminar-servicio/', eliminar_servicio_cumplido, name='eliminar_servicio_cumplido'),
    path('afiliados/<int:afiliado_id>/guardar-observacion/', guardar_observacion, name='guardar_observacion'),
    path("eliminar_todos_afiliados/", eliminar_todos_afiliados, name="eliminar_todos_afiliados"),
]
