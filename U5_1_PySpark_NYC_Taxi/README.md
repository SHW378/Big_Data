# U5: preparación de datos con PySpark (NYC Taxi)

Primer contacto con PySpark: se crea una `SparkSession` local, se leen columnas del archivo Parquet de viajes de taxi amarillo de Nueva York (enero 2025) directamente desde la web y se hacen agregaciones básicas.

```text
U5_1_PySpark_NYC_Taxi/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── U5_1_preparation_pyspark_NYC_taxi.ipynb
└── requirements.txt
```

## Requisitos

- Python 3.13 (el notebook menciona 3.12; con 3.13 también funciona).
- Java 17 o superior en el `PATH` (Spark lo necesita). Se probó con OpenJDK 21.

## Usar el notebook

En VS Code abre esta carpeta, abre el notebook y selecciona el kernel `Python 3.13 (U5 PySpark)` (en "Jupyter Kernel..."). Ese kernel define `PYSPARK_PYTHON` apuntando a `.venv`; sin esa variable Spark lanza el `python` del sistema y en Windows falla con "Python worker exited unexpectedly".

También se puede abrir con JupyterLab:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

## Recrear el entorno

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name u5-pyspark --display-name "Python 3.13 (U5 PySpark)"
```

Después agrega a `.venv\share\jupyter\kernels\u5-pyspark\kernel.json` la clave `"env"` con `PYSPARK_PYTHON` y `PYSPARK_DRIVER_PYTHON` igual a la ruta completa de `.venv\Scripts\python.exe`.

## Datos

El notebook no descarga el archivo completo: lee por rangos HTTP solo las columnas que necesita del Parquet publicado por la NYC TLC. Las carpetas `data/raw` y `data/processed` quedan para guardar datos locales si hacen falta; los CSV están excluidos de Git.
