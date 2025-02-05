from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator

# 定義 DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='basic_dag_example',
    default_args=default_args,
    schedule_interval='@daily',  # 每天運行一次
    catchup=False,
) as dag:

    # 定義任務
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    # 定義執行順序
    start >> end
