import csv
import requests
from weasyprint import HTML

# Path to your CSV file
csv_file = 'informador_links.csv'

# Define headers to mimic a full-size desktop browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                  'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                  'Chrome/117.0.0.0 Safari/537.36'
}

with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='|')
    for row in reader:
        url = row['link'].strip()
        if not url:
            continue

        # Generate a simple PDF filename based on the URL
        pdf_name = url.split('/')[-1] or "output"
        pdf_name = pdf_name.replace('.html', '')
        pdf_file = f"{pdf_name}.pdf"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                HTML(string=response.text, base_url=url).write_pdf(pdf_file)
                print(f"Converted {url} to {pdf_file}")
            else:
                print(f"Failed fetching {url}: status {response.status_code}")
        except Exception as e:
            print(f"Failed converting {url}: {e}")