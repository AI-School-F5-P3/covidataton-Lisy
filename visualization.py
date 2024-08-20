import matplotlib.pyplot as plt
import pandas as pd


def plot_state_data(covid_data, state):
    covid_data['date'] = pd.to_datetime(covid_data['date'], format='%Y%m%d')
    statewise_data = covid_data.groupby(['state', 'date']).sum().reset_index()
    state_data = statewise_data[statewise_data['state'] == state]

    plt.figure(figsize=(10, 6))
    plt.plot(state_data['date'], state_data['positiveIncrease'], label='Casos Diarios')
    plt.plot(state_data['date'], state_data['deathIncrease'], label='Muertes Diarias', color='red')
    plt.title(f'Evolución de Casos y Muertes Diarias en {state}')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Personas')
    plt.legend()
    plt.show()
