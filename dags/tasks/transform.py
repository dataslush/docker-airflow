from typing import Dict, List
from airflow.decorators import task

@task(multiple_outputs=True)
def transform(response: List[Dict]) -> List[str]:
    return {'title':res['title'] for res in response}
