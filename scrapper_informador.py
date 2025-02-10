import requests
from bs4 import BeautifulSoup
import time
import csv
import random

# Función para leer URLs desde un archivo CSV
def read_urls_from_csv(file_path):
    urls = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['processed'] == '0':
                urls.append(row)
    return urls

# Función para escribir URLs procesadas en el archivo CSV
def write_urls_to_csv(file_path, urls):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['link', 'processed', 'info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)  # Asegura que los valores se encierren en comillas dobles
        writer.writeheader()
        writer.writerows(urls)
        csvfile.close()

# Función para procesar una URL y extraer información
def process_url(url):
    # Hacer la solicitud HTTP
    response = requests.get(url['link'])

    # Verificar que la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Parsear el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontrar todos los elementos <p>
        paragraphs = soup.find_all("p")
        
        # Usar una lista para almacenar párrafos únicos
        unique_paragraphs = []

        # Filtrar y almacenar párrafos relevantes
        for paragraph in paragraphs:
            text = paragraph.text.strip()
            if text not in unique_paragraphs and not text.startswith("LEE:") and "Términos y Condiciones" not in text and len(text) >= 5 and not text.startswith("Por:"):
                unique_paragraphs.append(text)

        # Guardar la información extraída en la columna "info"
        url['info'] = " ".join(unique_paragraphs)  # Unir párrafos en un solo string

        # Marcar la URL como procesada
        url['processed'] = '1'
        print("Información extraída con exito.")
    else:
        print(f"Error al acceder a la página: {response.status_code}")
        url['info'] = "Error al acceder"

# Leer URLs desde el archivo CSV
urls = read_urls_from_csv("informador_links.csv")

# Procesar cada URL en la lista
for url in urls:
    print(f"Procesando URL: {url['link']}")
    process_url(url)
    print("\n" + "="*50 + "\n")
    time.sleep(random.randint(5, 10))

# Escribir las URLs actualizadas en el archivo CSV
write_urls_to_csv("informador_links.csv", urls)