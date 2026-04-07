from django.db import models
from datetime import datetime
# -----------------------------
# MODELO AFILIADO
# -----------------------------
class Afiliado(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    # Identificador automático
    id = models.BigAutoField(primary_key=True)

    dni = models.CharField(max_length=50, db_index=True, null=True, blank=True)  # No unique
    apellido_paterno = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    nombres = models.CharField(max_length=150, db_index=True, null=True, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)

    # Nuevos campos de observaciones: nullables en DB, blank en forms, default vacío
    observacion_enfermeria = models.TextField(blank=True, null=True, default="")
    observacion_odontologia = models.TextField(blank=True, null=True, default="")
    observacion_obstetricia = models.TextField(blank=True, null=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)  # registro en sistema
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.apellido_paterno or ''} {self.apellido_materno or ''}, {self.nombres or ''}"

    # -----------------------------
    # MÉTODOS ANUALES DE SERVICIOS
    # -----------------------------
    def servicios_del_anio(self, anio=None):
        """
        Devuelve servicios que el afiliado ya pasó en un año específico
        """
        if anio is None:
            anio = datetime.now().year
        return Servicio.objects.filter(
            atenciones__afiliado=self,
            atenciones__fecha_atencion__year=anio
        ).distinct()

    def servicios_pendientes_del_anio(self, anio=None):
        """
        Devuelve servicios que le faltan al afiliado en un año específico
        """
        servicios_todos = set(Servicio.objects.all())
        servicios_hechos = set(self.servicios_del_anio(anio))
        return servicios_todos - servicios_hechos



# -----------------------------
# MODELO SERVICIO
# -----------------------------
class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre



# -----------------------------
# MODELO ATENCION
# -----------------------------
class Atencion(models.Model):
    afiliado = models.ForeignKey(Afiliado, on_delete=models.CASCADE, related_name="atenciones")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="atenciones")
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    # 🔑 Nuevo campo: quién registró la atención
    registrado_por = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Registrado por"
    )

    class Meta:
        unique_together = ("afiliado", "servicio", "fecha_atencion")  # evita duplicados exactos

    def __str__(self):
        return f"{self.afiliado} - {self.servicio} ({self.fecha_atencion.date()})"

    def save_model(self, request, obj, form, change):
        if not obj.registrado_por:
            obj.registrado_por = request.user
        super().save_model(request, obj, form, change)
