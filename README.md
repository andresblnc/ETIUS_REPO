# REPOSITORIO DE CÓDIGOS PARA ETIUS OBSERVATORIO

#### Este repositorio contiene todos los programas y scripts desarrollados para el proyecto ETIUS Observatorio como parte del PAP (Proyecto de Aplicación Profesional).

## Descripción

El proyecto contiene códigos para hacer semanas compuestas en el programa random_dates.py, contiene un programa para poder hacer descargas en pdf de paginas de internet en el programa de link_to_pdf.py, contiene un separador de opciones de multiple opción de microsoft forms, esto para poder tener una columna con un 1 o 0 para cada opción un no una columnas con las opciones separadas por comas. 

Contiene tambien un programa para conseguir una lista de urls a partir de palabras clave, paginas especificas a buscar y fechas especificas y las entrega en un CSV. 

Además contiene codigos como webscrapper con 3 opciones diferentes que al final no fueron necesarios por lo que se encuentran en la carpeta de deprecated. 

## Instalación

Para utilizar los programas es requisito contar con Python instalado. Para configurar el entorno de desarrollo y ejecutar los programas de este repositorio, sigue estos pasos desde la terminal (o bash si estás en Windows). Para esto es necesario tener Git instalado:

1.  **Clona el repositorio:**
    ```bash
    git clone git@github.com:andresblnc/ETIUS_REPO.git
    cd ETIUS_REPO
    ```
2.  **Crea un entorno virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En macOS/Linux
    # venv\Scripts\activate  # En Windows
    ```
3.  **Instala las dependencias:**
    Asegúrate de tener `pip` actualizado (`pip install --upgrade pip`). Luego, instala las librerías necesarias desde el archivo [`requirements.txt`](requirements.txt):
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar cada uno de los programas es de la siguiente forma. 

```bash
python nombredelprograma.py
```

Para utilizar el programa de url_getter.py es necesario contar con una API_KEY para usar SerpAPI. Se puede conseguir una clave gratuita desde la página web indicada en el código. Esta clave debe colocarse dentro del archivo .env de la siguiente forma:y-a
```
SERPAPI_KEY=tu_key
```

Para ver como debe de funcionar la descarga de PDFs a partir de los links puedes ver el video de ejemplo en:
[`Ejemplo.mov`](Ejemplo.mov)

## Dependencias Principales

El proyecto utiliza varias librerías de Python, gestionadas a través de [`requirements.txt`](requirements.txt).