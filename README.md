# Metropolitano 🏥

Proyecto Django configurado para desarrollo local.

## 🚀 Comandos Rápidos

Si ya tienes el entorno configurado, solo corre esto:

```zsh
source venv/bin/activate
python manage.py runserver
```

Si prefieres usar **uv** directamente sin activar el entorno:

```zsh
uv run python manage.py runserver
```

---

## 🛠️ Configuración Inicial (en caso de error)

Si alguna dependencia falta o el entorno no funciona:

```zsh
# Crear entorno (si no existe)
uv venv

# Instalar dependencias
uv pip install -r requirements.txt
```

## 📂 Base de Datos
El proyecto está configurado para usar **SQLite** localmente (`db.sqlite3`).