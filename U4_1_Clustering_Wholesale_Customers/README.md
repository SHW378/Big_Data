# Clustering de Wholesale Customers

Entorno local: `.venv`, con Python 3.13, siguiendo la configuración de `U3_1_modelos_ml`.
Las dependencias del notebook están en `requirements.txt`.
Notebooks en `notebooks/`:

- `U4_1_Clustering_Wholesale_Customers.ipynb`
- `U4_2_Clustering_Online_Retail_Customers.ipynb`
- `U4_3_Plantilla_Clustering_Online_retail.ipynb`

Los notebooks de Online Retail leen `data/raw/online_retail.csv` y la plantilla
guarda los datos limpios en `data/processed/online_retail_limpios.csv`.

## Usar el notebook

Abre esta carpeta en VS Code. El intérprete predeterminado está configurado en
`.vscode/settings.json`. Si VS Code pide seleccionar un kernel, elige el Python
de `.venv/Scripts/python.exe`.

Para abrir JupyterLab desde PowerShell:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

El notebook descarga el conjunto de datos de UCI al ejecutarse y necesita conexión
a Internet para esa descarga.

## Recrear el entorno

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name u4-clustering --display-name "Python (.venv U4 Clustering)"
```

`.venv` es la carpeta del entorno virtual. No se necesita un archivo `.env` de
variables de entorno para este notebook.
