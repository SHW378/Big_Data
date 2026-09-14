from pathlib import Path
import json

import pandas as pd
import requests


# ============================================================
# 1. RUTAS Y DIRECCIONES DEL DATASET
# ============================================================

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
CARPETA_RAW = RAIZ_PROYECTO / "data" / "raw" / "alcohol"
CARPETA_PROCESSED = RAIZ_PROYECTO / "data" / "processed"

URL_DATOS = (
    "https://ourworldindata.org/grapher/"
    "share-of-adults-who-drank-alcohol-in-last-year.csv"
    "?v=1&csvType=full&useColumnShortNames=true"
)
URL_METADATA = (
    "https://ourworldindata.org/grapher/"
    "share-of-adults-who-drank-alcohol-in-last-year.metadata.json"
    "?v=1&csvType=full&useColumnShortNames=true"
)
VALOR_ORIGINAL = (
    "alcohol__consumers_past_12_months__pct__"
    "age_standardized__sex_both_sexes"
)


# ============================================================
# 2. DESCARGA DE DATOS Y METADATOS
# ============================================================

encabezados = {"User-Agent": "Our World In Data data fetch/1.0"}

df_original = pd.read_csv(URL_DATOS, storage_options=encabezados)

respuesta_metadata = requests.get(
    URL_METADATA,
    headers=encabezados,
    timeout=30,
)
respuesta_metadata.raise_for_status()
metadata = respuesta_metadata.json()


# ============================================================
# 3. RESPALDO DE LOS ARCHIVOS ORIGINALES
# ============================================================

CARPETA_RAW.mkdir(parents=True, exist_ok=True)
CARPETA_PROCESSED.mkdir(parents=True, exist_ok=True)

ruta_datos_raw = CARPETA_RAW / "alcohol_owid.csv"
ruta_metadata = CARPETA_RAW / "alcohol_owid.metadata.json"

df_original.to_csv(ruta_datos_raw, index=False)
with ruta_metadata.open("w", encoding="utf-8") as archivo:
    json.dump(metadata, archivo, ensure_ascii=False, indent=2)


# ============================================================
# 4. LIMPIEZA Y TRANSFORMACIÓN
# ============================================================

df = df_original.rename(columns={VALOR_ORIGINAL: "valor"})
df_paises = df.loc[df["code"].notna()].copy()
df_paises = df_paises.dropna(subset=["valor"]).drop_duplicates()

anio_mas_reciente = int(df_paises["year"].max())
ranking_2020 = (
    df_paises.loc[df_paises["year"] == anio_mas_reciente]
    .sort_values("valor", ascending=False)
    .reset_index(drop=True)
)
ranking_2020["posicion"] = ranking_2020.index + 1


# ============================================================
# 5. RESULTADO
# ============================================================

ruta_resultado = CARPETA_PROCESSED / "ranking_alcohol_2020.csv"
ranking_2020[["posicion", "entity", "code", "year", "valor"]].to_csv(
    ruta_resultado,
    index=False,
)

print("Pipeline ejecutado correctamente.")
print(f"Registros originales: {len(df_original):,}")
print(f"Países distintos: {df_paises['entity'].nunique()}")
print(f"Datos originales: {ruta_datos_raw}")
print(f"Metadatos: {ruta_metadata}")
print(f"Resultado: {ruta_resultado}")

