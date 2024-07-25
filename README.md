# ICA
The Air Quality Analysis Tool is a Python program that allows analyzing air quality data from CSV files. It provides functionalities to print detailed reports, evaluate air quality in different predefined ranges and generate visual graphs of the measurements, thus facilitating air pollution monitoring and analysis.
# Analizador de Calidad del Aire (ICA)

## Descripción

El Analizador de Calidad del Aire (ICA) es una herramienta en Python para analizar y visualizar datos de calidad del aire. El script permite cargar mediciones desde archivos, evaluar la calidad del aire basándose en rangos predefinidos, y generar gráficos de los datos de calidad del aire.

## Project Structure

ICA/
├── data/

│ ├── medidas.txt

│ └── rangos.txt
├── entorno_ICA/
├── src/
│ └── ICA.py
├── requirements.txt
├── LICENSE
├── README.md
└── .gitignore

vbnet
Copiar código

- **`data/`**: Contains the data files required for analysis.
  - `medidas.txt`: File with air quality measurements.
  - `rangos.txt`: File with air quality ranges.

- **`entorno_ICA/`**: (Optional) Directory for the virtual environment if used for the project.

- **`src/`**: Contains the project's source code.
  - `ICA.py`: Main script for air quality analysis.

- **`requirements.txt`**: File listing the dependencies required for the project.

- **`LICENSE`**: Project license file.

- **`README.md`**: This file with project documentation.

- **`.gitignore`**: File to specify which files or directories to ignore in Git.

## Requirements

The script requires Python and the `matplotlib` library. You can install the dependencies listed in `requirements.txt` using the following command:

```bash
pip install -r requirements.txt
The requirements.txt file should contain:

Copiar código
matplotlib
Data Files
The script uses two CSV data files:

data/medidas.txt: Contains air quality measurements. Each line should follow the format:

bash
Copiar código
date,so,pm10,pm25
Where:

date: The date of the measurement.
so: Sulfur dioxide (SO₂) measurement.
pm10: Particulate matter with diameter less than 10 micrometers.
pm25: Particulate matter with diameter less than 2.5 micrometers.
data/rangos.txt: Defines air quality ranges. Each line should follow the format:

Copiar código
quality,so2min,so2max,pm10min,pm10max,p25min,p25max
Where:

quality: Classification of air quality.
so2min and so2max: Range for SO₂.
pm10min and pm10max: Range for PM10.
p25min and p25max: Range for PM2.5.
Usage
Set Up the Environment:

Ensure you are in the root directory of the project (ICA/). If using a virtual environment, activate it.

Run the Script:

Navigate to the src/ directory and run the ICA.py script:

bash
Copiar código
cd src
python ICA.py
Provide File Names:

The script will prompt for data file names. You can press Enter to accept the default values (data/medidas.txt and data/rangos.txt) or enter different file names.

Select Menu Options:

After loading the files, the script will display a menu with the following options:

medidas: Displays the air quality measurements.
rangos: Displays the air quality ranges.
calidad: Evaluates and displays the air quality for each measurement based on the provided ranges.
grafica: Shows a graph of SO₂, PM10, and PM2.5 measurements.
salir: Exits the program.
Functions
mostrar_titulo(): Displays the program title.

recuperar_rangos(nombre_archivo): Reads air quality ranges from a CSV file.

imprimir_rangos(rangos): Prints air quality ranges in a tabular format.

recuperar_medidas(nombre_archivo): Reads air quality measurements from a CSV file.

imprimir_medidas(medidas): Prints air quality measurements in a tabular format.

getRangoSO(so, rangos): Determines the air quality for a given SO₂ measurement.

getRangoPM10(pm10, rangos): Determines the air quality for a given PM10 measurement.

getRangoPM25(pm25, rangos): Determines the air quality for a given PM2.5 measurement.

testear_calidad(medidas, rangos): Evaluates and displays air quality for all measurements based on the ranges.

graficas(medidas, rangos): Generates and displays graphs of SO₂, PM10, and PM2.5 measurements.

pedir_ficheros(): Prompts the user for data file names.

menuPrincipal(): Displays the main menu and returns the selected option by the user.

ejecutar_opcion(medidas, rangos, opcion): Executes the option selected by the user.

Contributing
If you want to contribute to the project, please fork the repository, make your changes, and submit a pull request with a detailed description of your modifications.

License
This project is licensed under the MIT License. See the LICENSE file for details.
