import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página a scrapear
url = 'https://covidtracking.com/data/national'

# Realizar la solicitud GET a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar la tabla que contiene los datos
    table = soup.find('table')  # Encuentra la primera tabla en la página
    
    # Extraer los encabezados de la tabla
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())
    
    # Extraer los datos de la tabla
    data = []
    for row in table.find_all('tr')[1:]:  # Omitir el encabezado
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
    
    # Crear un DataFrame con los datos
    df = pd.DataFrame(data, columns=headers)
    
    # Guardar los datos en archivos CSV
    df.to_csv('national_covid_data.csv', index=False)
    
    print("Datos guardados exitosamente en 'national_covid_data.csv'")
else:
    print(f"Error al acceder a la página: {response.status_code}")
