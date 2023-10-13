from google.cloud import bigquery

# Creamos el cliente de bigquery con el metodo Client
client = bigquery.Client()

def load_data(dataset_name, table_name, file_path):
    """
    Carga un archivo CSV en un dataset y tabla especificados de BigQuery.

    Args:
    - dataset_name (str): Nombre del dataset en BigQuery.
    - table_name (str): Nombre de la tabla dentro del dataset.
    - file_path (str): Ruta al archivo CSV que se cargará.

    Returns:
    - Resultado de la carga (google.cloud.bigquery.job.LoadJob).
    """

    # Especificar la ruta completa de la tabla en BigQuery (en la forma "project.dataset.table")
    table_id = f"{client.project}.{dataset_name}.{table_name}"

    # Crear un job_config para especificar el formato del archivo y otros detalles
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Ignorar la primera fila (encabezados)
        autodetect=True,  # Autodetecta el esquema (columnas y tipos) del CSV
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE # Configuración de carga con WRITE_TRUNCATE
    )

    # Cargar el archivo CSV desde la ruta especificada
    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    # Esperar a que el job se complete y devolver el resultado
    job.result()

    # Imprimir resultados
    print(f"Cargados {job.output_rows} rows en {table_id}.")

    return job