import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from weasyprint import HTML

# Path to your CSV file
csv_file = 'informador_links.csv'

# Configure Selenium for headless Chrome with a desktop viewport and user-agent
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                            "AppleWebKit/537.36 (KHTML, like Gecko) " +
                            "Chrome/117.0.0.0 Safari/537.36")

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

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
            driver.get(url)
            # Wait for the page to load completely
            time.sleep(2)  # You may adjust this delay or use explicit waits

            # Get the page source once fully loaded
            page_source = driver.page_source

            # Create a PDF from the HTML content
            HTML(string=page_source, base_url=url).write_pdf(pdf_file)
            print(f"Converted {url} to {pdf_file}")
        except Exception as e:
            print(f"Failed converting {url}: {e}")

driver.quit()