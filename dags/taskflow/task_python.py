from datetime import datetime
from airflow.decorators import dag, task

# 使用 @dag 裝飾器定義 DAG
@dag(
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={'owner': 'airflow'}
)
def python_taskflow_dag():

    # 使用 @task 裝飾器定義任務
    @task
    def say_hello():
        print("Hello, Airflow!")

    # 執行任務
    say_hello()

# 實例化 DAG
python_taskflow_dag = python_taskflow_dag()
