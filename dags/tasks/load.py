from typing import Dict, List
from airflow.decorators import task
from docker.types import Mount
from .settings import HOST_OUTPUT_DIR

@task.docker(
    image="load:latest",
    do_xcom_push=False,
    docker_url="unix://var/run/docker.sock",
    mount_tmp_dir=False,
    auto_remove=True,
    mounts=[
        Mount(
            source=HOST_OUTPUT_DIR, target="/home/datum-oracle/output", type="bind"
        )
    ]
)
def load(title):
    import pandas as pd
    df = pd.DataFrame([title])
    df.to_csv("output/titles.csv",index=False)