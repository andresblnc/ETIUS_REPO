import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Data/Analisis_Contenido.csv')

# Función para convertir una columna de opciones múltiples en columnas binarias
def expandir_opciones_multiples(dataframe, columna):
    # Obtener todas las opciones únicas en la columna
    todas_opciones = set()
    for opciones in dataframe[columna].dropna():
        for opcion in opciones.split(';'):
            todas_opciones.add(opcion.strip())
    
    # Crear columnas binarias para cada opción
    for opcion in todas_opciones:
        nombre_columna = f"{columna}_{opcion.replace(' ', '_')}"
        dataframe[nombre_columna] = dataframe[columna].apply(
            lambda x: 1 if isinstance(x, str) and opcion.strip() in [o.strip() for o in x.split(';')] else 0
        )
    
    return dataframe

# Ejemplo: expandir la columna "tipo_obra"
#df = expandir_opciones_multiples(df, "Actores sociales mencionados en la nota cultural:")

# Si tienes múltiples columnas de opción múltiple, puedes procesarlas todas
columnas_multiple_opcion = ["Actores sociales mencionados en la nota cultural:", "Público al que va dirigida la actividad o el artista al que se hace mención:", 'Disciplina artística mencionada en la nota:']
for col in columnas_multiple_opcion:
    df = expandir_opciones_multiples(df, col)

# Guardar el resultado
df.to_csv('Analisis_expandido.csv', index=False)
print("Proceso completado. Archivo guardado como 'Analisis_expandido.csv'")