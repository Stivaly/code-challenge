from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Importa tu función/script
from src.etl import run_etl_process

default_args = {
    'owner': 'StivalyG',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_dag',
    default_args=default_args,
    description='Un DAG para ejecutar el ETL cada hora',
    schedule_interval='@hourly',
    start_date=datetime(2023, 10, 12),
    catchup=False
)

run_etl = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl_process,
    dag=dag,
)

run_etl
