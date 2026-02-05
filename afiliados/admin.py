from django.contrib import admin
from .models import Afiliado, Servicio, Atencion

# -----------------------------
# ADMIN AFILIADO
# -----------------------------
@admin.register(Afiliado)
class AfiliadoAdmin(admin.ModelAdmin):
    list_display = ("id", "dni", "apellido_paterno", "apellido_materno", "nombres", "fecha_nacimiento", "sexo")
    search_fields = ("dni", "apellido_paterno", "apellido_materno", "nombres")
    list_filter = ("sexo",)
    ordering = ("apellido_paterno", "apellido_materno", "nombres")
    list_per_page = 50  # ajusta según tu preferencia

# -----------------------------
# ADMIN SERVICIO
# -----------------------------
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    ordering = ("nombre",)

# -----------------------------
# ADMIN ATENCION
# -----------------------------
@admin.register(Atencion)
class AtencionAdmin(admin.ModelAdmin):
    list_display = ("id", "afiliado", "servicio", "fecha_atencion", "registrado_por")
    search_fields = (
        "afiliado__dni",
        "afiliado__apellido_paterno",
        "afiliado__apellido_materno",
        "afiliado__nombres",
        "servicio__nombre",
    )
    list_filter = ("servicio", "fecha_atencion")
    ordering = ("-fecha_atencion",)
    list_per_page = 50
    readonly_fields = ("registrado_por",)  # lo muestra, pero no editable

    def save_model(self, request, obj, form, change):
        """
        Asigna automáticamente el usuario logueado como 'registrado_por'
        al crear o modificar una atención.
        """
        if not obj.registrado_por:
            obj.registrado_por = request.user
        super().save_model(request, obj, form, change)
