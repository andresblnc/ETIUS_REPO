import requests
from bs4 import BeautifulSoup
import time
import csv
import random

def read_urls_from_csv(file_path):
    with open(file_path, encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile, delimiter='|'))

def write_urls_to_csv(file_path, urls):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['link', 'processed', 'fecha', 'info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(urls)

def process_url(url):
    try:
        response = requests.get(url['link'], timeout=10)
        if not response.ok:
            raise Exception(f"Error HTTP: {response.status_code}")
            
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extraer fecha
        time_tag = soup.find('time', class_='news-date')
        if time_tag and time_tag.has_attr('datetime'):
            # Tomar solo la parte de la fecha antes de la T
            url['fecha'] = time_tag['datetime'].split('T')[0]
        else:
            url['fecha'] = 'No disponible'
        
        # Procesar párrafos sin saltos de línea
        seen = set()
        excluded_prefixes = ("LEE:", "Por:")
        paragraphs = []
        
        for p in soup.find_all("p"):
            # Remover saltos de línea y limpiar el texto
            text = p.text.replace("\n", " ").strip()
            if (text and text not in seen
                and not text.startswith(excluded_prefixes)
                and "Términos y Condiciones" not in text
                and len(text) >= 5):
                
                seen.add(text)
                paragraphs.append(text)
                
        url['info'] = ' '.join(paragraphs) or "Sin contenido válido"
        url['processed'] = '1'
        print(f"Extracción exitosa: {url['link']}")
        
    except Exception as e:
        print(f"Error procesando {url['link']}: {str(e)}")
        url['info'] = f"Error: {str(e)}"
        url['fecha'] = 'Error'

if __name__ == "__main__":
    urls = read_urls_from_csv("informador_links.csv")
    
    for url in urls:
        if url['processed'] == '0':
            print(f"\nProcesando: {url['link']}")
            process_url(url)
            time.sleep(random.randint(5, 10))
    
    write_urls_to_csv("informador_links.csv", urls)
    print("Proceso completado. Datos actualizados.")