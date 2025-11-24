from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests


DEFAULT_ARGS = {
'owner': 'airflow',
'depends_on_past': False,
'retries': 0,
}


with DAG('sdlc_agent_dag', start_date=datetime(2025,1,1), schedule_interval='@daily', default_args=DEFAULT_ARGS, catchup=False) as dag:
def trigger_agent(**kwargs):
resp = requests.post('http://sdlc-agent:8000/run', json={'task':'create_test_cases','context':'daily-run'})
print(resp.json())


run_task = PythonOperator(task_id='trigger_agent', python_callable=trigger_agent)


run_task
