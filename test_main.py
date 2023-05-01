from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_titles():
    response = client.get("/api/titles")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert len(data) == 1000


def test_get_all_titles_filtered():
    # test filtering when title_class == freehold
    response = client.get("/api/titles?title_class=freehold")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert len(data) == 513
    for title in data:
        assert title['title_class'] == 'Freehold'

    # test filtering when title_class == leasehold
    response = client.get("/api/titles?title_class=leasehold")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert len(data) == 487
    for title in data:
        assert title['title_class'] == 'Leasehold'


def test_get_all_titles_sort_by_id():
    # ascending
    response = client.get("/api/titles?_sort=id")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert len(data) == 1000
    # tests that ids are displayed ascending order
    for idx, title in enumerate(data):
        assert int(title['id']) == idx

    # descending
    response = client.get("/api/titles?_sort=id&_order=desc")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert len(data) == 1000
    # tests that ids are displayed descending order
    for idx, title in reversed(list(enumerate(data))):
        assert int(title['id']) == 999 - idx


def test_get_all_titles_paginated():
    response = client.get("/api/titles?_page=1&_limit=10")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert len(data) == 10


def test_get_all_titles_paginated():
    response = client.get("/api/titles/0")
    assert response.status_code == 200
    json_response = response.json()
    status = json_response['success']
    data = json_response['data']
    assert status == 'True'
    assert data == {
        "id": "0",
        "title_number": "MYBKZ10625",
        "title_class": "Freehold",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean convallis lectus velit, ac mollis lorem fringilla ac. In consequat molestie dui, et pellentesque nisl convallis at. Curabitur dictum lacinia justo, pulvinar pharetra purus ru"
    }
