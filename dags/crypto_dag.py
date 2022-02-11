from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
with DAG('crypto', start_date=datetime(2022, 1, 1)) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=print)