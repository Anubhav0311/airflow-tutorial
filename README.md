# airflow-tutorial

pkill -f "airflow scheduler"
pkill -f "airflow webserver"
airflow webserver -p 8080 -D
airflow scheduler -D
