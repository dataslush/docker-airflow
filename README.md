# docker-airflow
## Local Setup

Generate your own fernet key
---
```python
from cryptography.fernet import Fernet

fernet_key = Fernet.generate_key()
print(fernet_key.decode())
```
And place it under docker-compose **AIRFLOW__CORE__FERNET_KEY** variable

Setting the right Airflow User
---
[Follow the document](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#setting-the-right-airflow-user)

1. Copy sample.env to .env file
2. Run below command and replace the value with **AIRFLOW_UID**
```bash
id -u
```
3. Add path to host [output/](output) directory to **HOST_OUTPUT_DIR** env variable
4. Run below command to add permission to docker daemon so Airflow can run docker containers
```bash
bash bin/add_permission_docker_daemon.sh
```
5. Build Dockerfiles under [dockerfiles](dockerfiles)
```bash
docker build -f dockerfiles/load.Dockerfile -t load .
docker build -f dockerfiles/extract.Dockerfile -t extract .
```
6. Setup postgres Server, you can change Airflow username and password under **.env** file. This is one time setup.
```bash
bash bin/initial_setup.sh
```
7. Start and Stop the service by running respective commands
```bash
bash bin/start.sh # bash bin/stop.sh
```