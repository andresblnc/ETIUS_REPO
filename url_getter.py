# https://serpapi.com/search-api

import os
import csv
import serpapi
from dotenv import load_dotenv
load_dotenv()

CSV_PATH = "links.csv"
file_exists = os.path.isfile(CSV_PATH)

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

site = input("Ingrese el sitio web (ej. informador.mx): ")
keywords = input("Ingrese la palabra de busqueda (ej. agua, jalisco): ")


# Separamos las keywords y las encerramos entre comillas dobles
query = f"site:{site} {keywords}"
print("Query final:", query)
print()

months = int(input("Meses atras a buscar: "))
total = int(input("Numero de resultados a buscar: "))

results = client.search(
    q=query,
    engine="google",
    hl="es",
    num=total,
    as_qdr=f"m{months}"
)

# Si no encuentra información o hay errores.
if 'error' in results:
    print("Error:", results['error'])
    exit()

results = results['organic_results']

# Antes de abrir el archivo, verificamos que si ya existe y no termina en salto de línea, lo agregamos
if file_exists and os.stat(CSV_PATH).st_size > 0:
    with open(CSV_PATH, "rb") as f:
        f.seek(-1, os.SEEK_END)
        if f.read(1) != b'\n':
            with open(CSV_PATH, "a", newline="") as csvfile:
                csvfile.write("\n")

# Guardamos los resultados en el CSV siguiendo el formato: link|processed
with open(CSV_PATH, "a", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter="|")
    for result in results:
        link = result['link']
        writer.writerow([link, 0])