import tasks
from celery import Celery, chain, group



# chain()


for i in range(50000):
    print(i)
    tasks.get_mock1.delay(i)