from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# 定義 Python 函數
def process_item(item):
    print(f"Processing item: {item}")

# 定義 DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='dynamic_task_mapping_example',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    # 定義動態任務映射
    process_tasks = PythonOperator.partial(
        task_id='process_task',
        python_callable=process_item,
    ).expand(op_args=[[1, 2, 3, 4]])  # 動態生成四個任務
