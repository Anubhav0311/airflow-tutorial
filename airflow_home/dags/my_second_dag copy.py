from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_third_dag',
    default_args=default_args,
    description='A simple DAG in workspace',
    schedule_interval=timedelta(days=1),
)

def print_hello():
    print("Hello, Airflow from the workspace! 🚀")

hello_task = PythonOperator(
    task_id='print_hello_task',
    python_callable=print_hello,
    dag=dag,
)

def print_hi():
    print("Hi, Airflow from the workspace! 🚀")

hi_task = PythonOperator(
    task_id='print_hi_task',
    python_callable=print_hi,
    dag=dag,
)

hello_task >> hi_task