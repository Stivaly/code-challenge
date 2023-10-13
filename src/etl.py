from bigquery_utils import load_data
import pandas as pd
import os

# Realizamos referencia a nuestra llave
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/etl-code-challenge-42c88c66e88d.json"
# Creamos rutas relativas en el entorno
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '..', 'data', 'source', 'online_retail.csv')


def extract():
    try:
        # Leer el archivo CSV con el Framework PANDAS
        online_retail = pd.read_csv(file_path, encoding='utf-8')
        return online_retail
    except Exception as e:
        print(f"Error durante la extracción: {e}")
        raise

def transform(online_retail):
    # Operaciones de limpieza y transformación para archivo de Retail de ventas
    try:
        """
        Durante la exploracion en python shell pude detectar inconsistencias en algunos campos con una letra adicional,
        al verificar no afecta quitar esta letra y nos permite cambiar el campo InvoiceNo a numero, manteniendo sus valores sin duplicidad
        """
        online_retail['InvoiceNo'] = online_retail['InvoiceNo'].str.replace('[a-zA-Z]', '', regex=True)
        # Damos los formatos correctos a las columnas para poder ser procesadas correctamente en BigQuery
        online_retail['InvoiceNo'] = online_retail['InvoiceNo'].astype(int)
        online_retail['InvoiceDate'] = pd.to_datetime(online_retail['InvoiceDate'])


        # Eliminar registros duplicados, solo cuando todos los campos son exactamente iguales
        online_retail.drop_duplicates(inplace=True)

        # Reemplazo de valores faltantes en columnas numéricas con 0
        numerical_columns = ['InvoiceNo', 'Quantity', 'UnitPrice', 'CustomerID']
        online_retail[numerical_columns] = online_retail[numerical_columns].fillna(0)

        # Reemplazo de valores faltantes en columnas string con 'sin información'
        some_columns = ['StockCode', 'Description', 'Country']
        online_retail[some_columns] = online_retail[some_columns].fillna('sin informacion')

        #Detectamos que la columna description tiene comillas simples que estan generando errores de cargado, usamos el siguiente codigo para reemplazar las comillas simples y dobles
        online_retail['Description'] = online_retail['Description'].str.replace('["\']', '', regex=True)

        return online_retail
    except Exception as e:
        print(f"Error durante la transformación: {e}")
        raise

def prepare():
    try:
        #Transformamos archivo a CSV para su facilidad de subida
        online_retail = extract()
        processed_online_retail = transform(online_retail)

        # Obtenemos la ubicación del directorio del script
        script_dir = os.path.dirname(__file__)

        # Construimos la ruta completa al archivo de salida
        output_file_path = os.path.join(script_dir, '..', 'data', 'temporales', 'temp_data.csv')

        # Guardamos el DataFrame en el archivo CSV
        processed_online_retail.to_csv(output_file_path, index=False, encoding='utf-8')

        return processed_online_retail, output_file_path
    except Exception as e:
        print(f"Error durante la preparación: {e}")
        raise

def run_etl_process():
    try:
        prepared_data, output_file_path = prepare()
        load_data('online_retail', 'sales_transaction', output_file_path)
    except Exception as e:
        print(f"Error general en el ETL: {e}")