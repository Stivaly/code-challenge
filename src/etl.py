import pandas as pd
import os
# Realizamos referencia a nuestra llave
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/etl-code-challenge-42c88c66e88d.json"


def extract_and_process(file):
    # Leer el archivo CSV con el Framework PANDAS
    online_retail = pd.read_csv(file, encoding='utf-8')

    # Operaciones básicas de limpieza y transformación para archivo de Retail de ventas entre 01/12/2010 y 09/12/2011
    # Eliminar registros duplicados
    online_retail.drop_duplicates(inplace=True)

    # Reemplazo de valores faltantes en columnas numéricas con 0
    numerical_columns = online_retail.select_dtypes(include=['number']).columns
    online_retail[numerical_columns] = online_retail[numerical_columns].fillna(0)

    # Reemplazo de valores faltantes en columnas tipo object con 'sin información'
    object_columns = online_retail.select_dtypes(include=['object']).columns
    online_retail[object_columns] = online_retail[object_columns].fillna('sin informacion')

    return online_retail

# Ejecutar la función
processed_online_retail = extract_and_process("../data/source/online_retail.csv")

prueba = processed_online_retail.query("CustomerID == 'sin informacion'")
print(prueba.head())