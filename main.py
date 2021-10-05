import requests


url = 'http://localhost:8000/api'


def get_mock1(id):
    res = requests.get(f'{url}/mock1/{id}')
    if res.ok:
        print(res.text)
        return res.text
    else:
        return None


def get_mock2(content):
    res = requests.get(f'{url}/mock2/{content}')
    if res.ok:
        print(res.text)
    else:
        print('error')


mock1_data = get_mock1(123)

if mock1_data != None:
    get_mock2(mock1_data)