from pytest import fixture
import requests
import json


@fixture(scope='module')
def request_utility_post():
    def wrapper(url, **payload):
        headers = {
            'Accept': 'application/json, */*',
            'Content-Type': 'application/json'
        }
        return requests.post(url, data=json.dumps(payload), headers=headers)
    return wrapper


@fixture(scope='module')
def request_utility_get():
    def wrapper(url, kwargs):
        return requests.get(f"{url}{kwargs}")
    return wrapper


@fixture(scope='module')
def request_utility_delete():
    def wrapper(url, kwargs):
        return requests.delete(f"{url}{kwargs}")
    return wrapper


@fixture(scope='module', params=['976308'])
def pet_id(request):
    return request.param