from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Function to decide which path to take
def check_data():
    import random
    data_valid = random.choice([True, False])  # Randomly simulate valid/invalid data
    return "process_data" if data_valid else "send_alert"

# Dummy function for processing
def process_data():
    print("Processing valid data...")

# Dummy function for sending alert
def send_alert():
    print("Sending alert: Data is invalid!")

# Define DAG
dag = DAG(
    'conditional_branching_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 3, 30),
    catchup=False
)

# Start task
start = DummyOperator(task_id="start", dag=dag)

# Task to check data validity
check_data_task = BranchPythonOperator(
    task_id='check_data',
    python_callable=check_data,
    dag=dag
)

# Processing valid data
process_task = PythonOperator(task_id='process_data', python_callable=process_data, dag=dag)

# Sending alert for invalid data
alert_task = PythonOperator(task_id='send_alert', python_callable=send_alert, dag=dag)

# End task
end = DummyOperator(task_id="end", dag=dag)

# Define flow
start >> check_data_task
check_data_task >> process_task >> end
check_data_task >> alert_task >> end