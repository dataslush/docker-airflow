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