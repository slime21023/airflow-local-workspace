from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator

# 定義分支邏輯
def choose_branch(**kwargs):
    # 根據條件選擇分支
    return 'branch_a' if kwargs['logical_condition'] else 'branch_b'

# 定義 DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='branching_example',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    start = DummyOperator(task_id='start')

    # 分支邏輯
    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=choose_branch,
        op_kwargs={'logical_condition': True},  # 傳遞條件
    )

    branch_a = DummyOperator(task_id='branch_a')
    branch_b = DummyOperator(task_id='branch_b')

    join = DummyOperator(task_id='join', trigger_rule='none_failed_or_skipped')

    # 定義執行順序
    start >> branching
    branching >> [branch_a, branch_b] >> join
