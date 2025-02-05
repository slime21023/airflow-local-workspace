from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator

# 使用 @dag 裝飾器定義 DAG
@dag(
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    default_args={'owner': 'airflow'}
)
def branching_taskflow_dag():

    # 定義條件分支邏輯
    @task.branch
    def choose_branch(logical_condition: bool):
        return 'branch_a' if logical_condition else 'branch_b'

    @task
    def branch_a():
        print("Branch A executed.")

    @task
    def branch_b():
        print("Branch B executed.")

    # 定義開始與結束節點
    start = EmptyOperator(task_id='start')
    join = EmptyOperator(task_id='join', trigger_rule='none_failed_or_skipped')

    # 定義執行順序
    start >> choose_branch(True) >> [branch_a(), branch_b()] >> join

# 實例化 DAG
branching_taskflow_dag = branching_taskflow_dag()
