from datetime import datetime
from airflow.decorators import dag, task
from airflow.utils.task_group import TaskGroup

# 使用 @dag 裝飾器定義 DAG
@dag(
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={'owner': 'airflow'}
)
def task_group_taskflow_dag():

    # 定義開始與結束任務
    @task
    def start():
        print("Start task executed.")

    @task
    def end():
        print("End task executed.")

    # 定義任務分組
    with TaskGroup(group_id='data_processing') as data_processing:
        @task
        def extract():
            print("Extracting data.")

        @task
        def transform():
            print("Transforming data.")

        @task
        def load():
            print("Loading data.")

        extract() >> transform() >> load()

    # 定義執行順序
    start() >> data_processing >> end()

# 實例化 DAG
task_group_taskflow_dag = task_group_taskflow_dag()
