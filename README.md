# Metropolitano 🏥 - Sistema de Gestión Médica

Sistema robusto y moderno para la gestión de afiliados, atenciones médicas e importación masiva de datos mediante Excel. Diseñado para ofrecer una experiencia de usuario premium con tiempos de respuesta optimizados y una interfaz dinámica.

## 🛠️ Stack Tecnológico

El proyecto utiliza tecnologías de vanguardia para garantizar estabilidad y escalabilidad:

### **Backend**
- **Framework:** [Django 6.0+](https://www.djangoproject.com/)
- **Procesamiento de Datos:** [Pandas](https://pandas.pydata.org/) (para importación inteligente de Excel)
- **Gestión de Entorno:** [uv](https://github.com/astral-sh/uv) (Package manager ultrarrápido)

### **Frontend (Premium UI/UX)**
- **Estilos:** [Tailwind CSS](https://tailwindcss.com/) (vía CDN para máximo rendimiento)
- **Tablas Dinámicas:** [DataTables.js](https://datatables.net/) (con procesamiento del lado del servidor)
- **Interacciones:** [SweetAlert2](https://sweetalert2.github.io/) y [AJAX](https://api.jquery.com/jquery.ajax/)
- **Iconografía:** [FontAwesome 6+](https://fontawesome.com/)

### **Infraestructura y Base de Datos**
- **Base de Datos (Híbrida):**
  - **Desarrollo:** [SQLite](https://www.sqlite.org/) (rápido y portable)
  - **Producción:** [Neon Postgres](https://neon.tech/) (Serverless PostgreSQL)
- **Servidor / Hosting:** [Vercel](https://vercel.com/)
- **Archivos Estáticos:** [WhiteNoise](http://whitenoise.evans.io/en/stable/) (optimizado para entornos Serverless)

---

## 🚀 Inicio Rápido (Local)

### 1. Clonar y Preparar Entorno
Si usas **uv** (recomendado):
```zsh
# Crear entorno virtual e instalar dependencias
uv venv
uv pip install -r requirements.txt
```

### 2. Configuración de Variables
Crea un archivo `.env` en la raíz (usa `.env.example` como base si existe):
```env
DEBUG=True
SECRET_KEY=tu_clave_secreta
# Si quieres usar la DB de Neon localmente:
DATABASE_URL=postgres://tu_url_de_neon
```

### 3. Ejecutar Servidor
```zsh
uv run python manage.py runserver
```
Accede a: `http://127.0.0.1:8000`

---

## 🌐 Despliegue en Vercel

El proyecto está configurado para "Zero Configuration" en Vercel:

1.  **Variables de Entorno:** Asegúrate de que `DATABASE_URL` esté configurada en el panel de Vercel (Storage -> Connect).
2.  **Archivos Estáticos:** WhiteNoise se encarga automáticamente de servir los estilos del admin de Django sin necesidad de servidores externos.
3.  **Base de Datos:** La lógica híbrida en `settings.py` detectará automáticamente cuándo usar Postgres (Vercel) y cuándo SQLite (Local).

### Comandos de Mantenimiento en Producción:
Para aplicar migraciones en el servidor de Neon:
```zsh
# Desde local (con el .env de producción activo)
python manage.py migrate
```

---

## 📂 Estructura del Proyecto
- `/afiliados`: Lógica de negocio (Modelos, Vistas y lógica de importación).
- `/metropolitano`: Configuración central del proyecto Django.
- `/templates`: Interfaces HTML dinámicas.
- `/static`: Assets locales (imágenes y recursos base).

---

© 2026 Metropolitano Data Systems. Todos los derechos reservados.