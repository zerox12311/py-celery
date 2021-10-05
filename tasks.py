import requests
from celery import Celery, chain, group


app = Celery(
    'hello',
    broker='pyamqp://server:PASSW0RD@localhost:5672',
    result_backend='redis://localhost:6379/0')



url = 'http://localhost:8000/api'


@app.task(autoretry_for=(Exception, ), default_retry_delay=1, max_retries=None)
def get_mock1(id):
    res = requests.get(f'{url}/mock1/{id}')
    if res.ok:
        print(res.text)
        return res.text
    else:
        raise Exception(f'Mock1 Error')

@app.task(autoretry_for=(Exception, ), default_retry_delay=1, max_retries=None)
def get_mock2(content):
    res = requests.get(f'{url}/mock2/{content}')
    if res.ok:
        print(res.text)
    else:
        raise Exception(f'Mock2 Error')