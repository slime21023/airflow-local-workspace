from datetime import datetime
from airflow.decorators import dag, task

@dag(
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={'owner': 'airflow'}
)
def basic_taskflow_dag():
    @task()
    def start():
        print("Start task executed.")

    @task()
    def end():
        print("End task executed.")

    start() >> end()

# 實例化 DAG
basic_taskflow_dag = basic_taskflow_dag()