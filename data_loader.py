import pandas as pd
import requests

def load_covid_data():
    url = "https://api.covidtracking.com/v1/states/daily.json"
    response = requests.get(url)

    if response.status_code == 200:
        covid_data = pd.DataFrame(response.json())
        print("Datos cargados exitosamente.")
        return covid_data
    else:
        print(f"Error al cargar los datos: {response.status_code}")
        return None



