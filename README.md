# Big Data

Repositorio de prácticas y proyectos desarrollados durante la materia de **Big Data**.

## Descripción

Este repositorio contiene las prácticas, ejercicios y proyectos realizados durante el curso.
Cada práctica se plantea como un proyecto de datos independiente, con sus propios datos,
código, dependencias y entorno de ejecución.

El repositorio permite mantener un registro de la evolución del trabajo mediante Git y GitHub.

## Prácticas

| Carpeta | Tema | Dataset |
|---|---|---|
| [`U-1-2-PRUEBA`](U-1-2-PRUEBA/) | Probabilidad y estadística | Población mundial (Our World in Data / UN WPP 2024) |
| [`Examen Práctico Topicos de Big Data`](<Examen Práctico Topicos de Big Data/>) | Examen práctico, primer parcial | Consumo de alcohol en adultos |
| [`U3_1_modelos_ml`](U3_1_modelos_ml/) | Regresión lineal, polinomial y Random Forest | Nacimientos y defunciones en México |
| [`U4_1_Clustering_Wholesale_Customers`](U4_1_Clustering_Wholesale_Customers/) | Clustering con K-Means | Wholesale Customers y Online Retail |

## Estructura del repositorio

Cada carpeta corresponde a una práctica o proyecto independiente:

```text
Bid_Data/
├── U-1-2-PRUEBA/
├── Examen Práctico Topicos de Big Data/
├── U3_1_modelos_ml/
├── U4_1_Clustering_Wholesale_Customers/
└── README.md
```

Dentro de cada práctica se sigue, en general, esta organización:

```text
practica/
├── data/
│   ├── raw/          # datos originales
│   └── processed/    # datos limpios
├── notebooks/        # notebooks de Jupyter
├── src/              # código de apoyo
├── requirements.txt  # dependencias
└── README.md         # instrucciones de la práctica
```
