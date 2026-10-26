# BigData Parcial 2

Entorno local: `.venv`, con Python 3.13, siguiendo la configuración de
`U4_1_Clustering_Wholesale_Customers`. Las dependencias están en `requirements.txt`.

Estructura:

- `notebooks/`: notebooks del parcial.
- `data/raw/`: datos originales.
- `data/processed/`: datos limpios o transformados.

## Usar el notebook

Abre esta carpeta en VS Code. El intérprete predeterminado está configurado en
`.vscode/settings.json`. Si VS Code pide seleccionar un kernel, elige el Python
de `.venv/Scripts/python.exe`.

Para abrir JupyterLab desde PowerShell:

```powershell
.\.venv\Scripts\python.exe -m jupyterlab notebooks
```

## Recrear el entorno

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name bigdata-parcial2 --display-name "Python (.venv BigData Parcial2)"
```

`.venv` es la carpeta del entorno virtual. No se necesita un archivo `.env` de
variables de entorno.
