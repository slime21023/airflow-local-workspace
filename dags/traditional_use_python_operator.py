from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# 定義 Python 函數
def print_hello():
    print("Hello, Airflow!")

# 定義 DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='python_operator_example',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # 定義任務
    hello_task = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello,  # 指定要執行的 Python 函數
    )
