import pytest


def test_get_non_existent_post(api_client):
    """получить несуществующий пост"""

    response = api_client.get("/posts/9999")

    assert response.status_code == 404


def test_get_non_existent_users(api_client):
    """получить несуществующий пользователь"""

    response = api_client.get("/users/9999")

    assert response.status_code == 404


def test_get_non_existent_todo(api_client):
    """получить несуществующую задачу"""

    response = api_client.get("/todos/9999")

    assert response.status_code == 404


def test_get_non_existent_endpoint(api_client):
    """получить несуществующий эндпоинт"""

    response = api_client.get("/nonexistent")

    assert response.status_code == 404


def test_create_post_with_invalid_data(api_client):
    """создать пост с невалидными данными"""
    """
    jsonplaceholder не валидириует тело запроса,
    поэтому возвращает 201, а не 400
    """

    payload = {
        "title": 123,  # должно быть строкой
        "body": True,  # должно быть строкой
        "userId": "abc"  # должно быть числом
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201


def test_create_post_without_payload(api_client):
    """создать пост без данных"""
    """
    jsonplaceholder не валидириует тело запроса,
    поэтому возвращает 201, а не 400
    """

    response = api_client.post("/posts")

    assert response.status_code == 201


def test_get_post_with_string_id(api_client):
    """получить пост с строковым ID"""
    
    response = api_client.get("/posts/abc")
    assert response.status_code == 404