# U3: modelos de regresión y demografía

Práctica de comparación de regresión lineal, regresión polinomial y Random Forest para nacimientos y defunciones en México. El notebook incluye las respuestas a las preguntas de observación y reflexión.

```text
U3_1_modelos_ml/
├── data/          # Archivos de datos
├── src/           # Código Python auxiliar
├── notebooks/
│   └── U3_1_modelos_regresion_demografia.ipynb
└── requirements.txt
```

## Preparar el entorno

Se verificaron las dependencias con Python 3.13. Desde esta carpeta, en PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

El entorno `.venv` se crea localmente y está excluido de Git. Los archivos `.gitkeep` permiten conservar las carpetas `data` y `src` mientras estén vacías.

## Abrir el notebook

```powershell
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

En VS Code, abre esta carpeta, abre el notebook y selecciona `.venv\Scripts\python.exe` como entorno del kernel.

## Datos

El notebook descarga los datos desde Our World in Data al ejecutarse. Su alternativa local busca `births-and-deaths-projected-to-2100.csv` en el directorio de ejecución; si guardas el CSV en `data/` y ejecutas desde `notebooks/`, cambia esa lectura a `../data/births-and-deaths-projected-to-2100.csv`.
