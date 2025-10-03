import pandas as pd
import numpy as np

# Definición del nombre de la hoja en el archivo Excel
NOMBRE_HOJA = 'Listado'

# ---
# 1. Cargar el archivo Excel, forzando 'DNI' a ser un string (object)
try:
    # Definimos explícitamente los tipos de datos para asegurar el formato correcto
    dtype_config = {
        'DNI': str,
        'APE PATERNO': str,
        'APE MATERNO': str,
        'NOMBRES': str,
        'SEXO': str
    }
    
    # Cargamos el DataFrame especificando la hoja, los tipos de datos y el parseo de la fecha
    df = pd.read_excel(
        'data.xlsx',
        sheet_name=NOMBRE_HOJA, # <--- MODIFICACIÓN CLAVE: Especificar la hoja
        dtype=dtype_config,
        parse_dates=['FECHA NAC']
    )
    print(f"✅ Archivo 'data.xlsx' cargado exitosamente desde la hoja '{NOMBRE_HOJA}'.")
except FileNotFoundError:
    print("❌ ERROR: El archivo 'data.xlsx' no se encontró. Asegúrate de que esté en el mismo directorio.")
    exit()
except ValueError as e:
    # Esto captura errores si la hoja no existe
    if 'Worksheet' in str(e) and 'not found' in str(e):
        print(f"❌ ERROR: No se encontró la hoja '{NOMBRE_HOJA}' en el archivo. Verifica el nombre.")
    else:
        print(f"❌ ERROR al cargar los datos: {e}")
    exit()

# ---
print("\n" + "="*50)
print("🔎 1. Verificación de Campos Vacíos (Valores Faltantes)")
print("="*50)

# 2. Conteo de valores nulos (vacíos) por columna
# Esto incluye tanto NaN de Pandas como strings vacíos si Pandas los lee como NaN
campos_vacios = df.isnull().sum()

# 3. Mostrar el resultado
if campos_vacios.sum() == 0:
    print("¡🎉 EXCELENTE! No se encontraron campos vacíos (NaN) en ninguna columna.")
else:
    print("⚠️ ¡ATENCIÓN! Se encontraron los siguientes campos vacíos:")
    # Solo muestra las columnas con valores nulos y su conteo
    print(campos_vacios[campos_vacios > 0]) 

# ---
print("\n" + "="*50)
print("📊 2. Revisión Final de Tipos de Datos y Consistencia de DNI")
print("="*50)

# 4. Revisión de los tipos de datos para confirmar la carga
tipos_de_datos = df.dtypes

# 5. Mostrar el resultado de tipos
print("Tipos de datos actuales. Confirma que 'DNI' sea 'object' y 'FECHA NAC' sea 'datetime':")
print(tipos_de_datos)

# 6. Verificación de la longitud del DNI
print("\n--- Verificación de 'DNI' ---")
# Filtramos los valores nulos antes de calcular la longitud para evitar errores
df_dni_valido = df.dropna(subset=['DNI'])

if not df_dni_valido.empty:
    long_min = df_dni_valido['DNI'].astype(str).str.len().min()
    long_max = df_dni_valido['DNI'].astype(str).str.len().max()
    print(f"La longitud mínima del DNI (sin contar vacíos) es: {long_min}")
    print(f"La longitud máxima del DNI (sin contar vacíos) es: {long_max}")
    print("Longitud ideal del DNI Peruano es de 8 dígitos. Cualquier otra longitud indica un potencial error.")
else:
    print("No hay valores de DNI no vacíos para verificar la longitud.")
print("----------------------------")