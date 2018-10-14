import requests
from requests.auth import HTTPBasicAuth
from json import dumps


def test_hello_service_get():
    user = 'tomer'
    password = 'cool'
    res = requests.get('http://app:8083', auth=HTTPBasicAuth(user, password))
    assert res.text == 'hello world', 'Expecting:  "hello world", Actual: {0}'.format(res.text)


def test_ping_service_get():
    res = requests.get('http://app:8083/ping')
    assert res.text == 'pong', 'Expecting: "pong", Actual: {0}'.format(res.text)


def test_get_all_tasks_service_get():
    res = requests.get('http://app:8083/todo/api/v1.0/tasks')
    assert res.text and res.status_code == 200


def test_get_a_task_service_get():
    task_id = 1
    res = requests.get('http://app:8083/todo/api/v1.0/tasks/{0}'.format(task_id))
    json = res.json()
    results = json['task']['id']
    assert results == task_id and res.text and res.status_code == 200


def test_add_task_service_post():
    url = "http://app:8083/todo/api/v1.0/tasks"
    data = {'title': 'Read a book'}
    headers = {'Content-type': 'application/json'}
    res = requests.post(url=url, data=dumps(data), headers=headers)
    assert res.reason == 'CREATED' and res.text
