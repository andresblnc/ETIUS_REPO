# Es necesario poner el teclado en ingles y no poner en pantalla completa. 
import pyautogui
import time
import csv

# Path to your CSV file
csv_file = 'links.csv'

# pyautogui.displayMousePosition()

# open safari
pyautogui.keyDown('command')
pyautogui.press('space')
pyautogui.keyUp('command')
time.sleep(1)
pyautogui.write('safari')
pyautogui.press('enter')
time.sleep(2)


# For every row in the CSV file get the link and open it in Safari
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='|')
    for row in reader:  
        url = row['link'].strip()
        if not url:
            continue
        
        # Open a new tab in Safari
        pyautogui.click(1400, 65)
        time.sleep(1)
        pyautogui.write(url)
        pyautogui.press('enter')
        time.sleep(6)

        # Choose to print page
        pyautogui.keyDown('command')
        pyautogui.press('p')
        pyautogui.keyUp('command')
        time.sleep(2)

        # Choose to save as PDF
        pyautogui.click(681, 847)
        time.sleep(2)

        # # Write name of the file
        # pyautogui.write(url)
        # time.sleep(2)

        # Search folder
        time.sleep(1)
        pyautogui.click(1125, 223)
        time.sleep(1)
        pyautogui.write('ETIUS_PDFs')

        # Select Folder & Save
        time.sleep(2)
        pyautogui.click(436, 330)
        time.sleep(1)
        pyautogui.click(1220, 758)
        time.sleep(4)

        # Close tab
        pyautogui.click(589, 65)
        time.sleep(1)
    
    print('Registro de PDFS finalizado')