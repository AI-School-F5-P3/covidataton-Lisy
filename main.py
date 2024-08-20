from data_loader import load_covid_data
from data_exploration import explore_data
from visualization import plot_state_data
from report_generator import generate_report

def main():
    # Cargar los datos desde la API
    covid_data = load_covid_data()
    print("Datos cargados exitosamente.")
    print(covid_data.info())

    # Explorar los datos
    explore_data(covid_data)

     # Guardar los datos en un archivo CSV
    output_file = 'covid_data_processed.csv'
    covid_data.to_csv(output_file, index=False)  # index=False para no guardar el índice en el CSV
    
    print(f"Datos guardados en {output_file}.")

    # Visualizar los datos para un estado específico
    plot_state_data(covid_data, 'NY')

    # Generar el informe
    generate_report(covid_data)

if __name__ == "__main__":
    main()
