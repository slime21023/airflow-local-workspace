from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup

# 定義 DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='task_group_example',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    start = DummyOperator(task_id='start')

    # 定義 Task Group
    with TaskGroup(group_id='data_processing') as data_processing:
        extract = DummyOperator(task_id='extract')
        transform = DummyOperator(task_id='transform')
        load = DummyOperator(task_id='load')

        extract >> transform >> load

    end = DummyOperator(task_id='end')

    # 定義執行順序
    start >> data_processing >> end
