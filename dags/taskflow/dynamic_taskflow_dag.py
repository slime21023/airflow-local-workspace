from datetime import datetime
from airflow.decorators import dag, task

# 使用 @dag 裝飾器定義 DAG
@dag(
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={'owner': 'airflow'}
)
def dynamic_taskflow_dag():

    # 使用 @task 裝飾器定義任務
    @task
    def process_item(item):
        print(f"Processing item: {item}")

    # 動態生成任務
    process_item.expand(item=[1, 2, 3, 4])

# 實例化 DAG
dynamic_taskflow_dag = dynamic_taskflow_dag()
