from typing import Dict, List
from airflow.decorators import task

@task.docker(
    image="extract:latest",
    multiple_outputs=True,
    do_xcom_push=False,
    docker_url="unix://var/run/docker.sock",
    mount_tmp_dir=False,
    auto_remove=True
)
def extract():
    import requests
    import json
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    return {'response':res.json()}