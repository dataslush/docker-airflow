from airflow.decorators import dag, task
from datetime import datetime, timedelta

from tasks import extract, transform, load

@dag(
    schedule_interval=None,
    start_date=datetime(2022, 7, 30),
    concurrency=1,
    max_active_runs=1,
)
def etl():
    load(transform(extract()['response']))


etl_dag = etl()