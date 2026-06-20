from models.post import PostSchema
import pytest


def test_get_posts(api_client):
    """получить список всех постов"""

    response = api_client.get("/posts")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for post in response.json():
        PostSchema(**post)


@pytest.mark.parametrize(
        "user_id", 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_posts_by_user_id(api_client, user_id):
    """получить список всех постов пользователя"""

    response = api_client.get(f"/users/{user_id}/posts")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for post in response.json():
        validated = PostSchema(**post)
        assert validated.userId == user_id


@pytest.mark.parametrize(
        "post_id",
        [5, 12, 27, 43, 56, 61, 78, 82, 90, 99]
    )
def test_get_post_by_id(api_client, post_id):
    """получить пост по его ID"""
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200

    post = PostSchema(**response.json())

    assert post.id == post_id


def test_create_post(api_client, payload):
    """создать пост"""

    response = api_client.post("/posts", json=payload)
    assert response.status_code == 201

    data = PostSchema(**response.json())

    assert data.id == 101
    assert data.title == payload["title"]
    assert data.body == payload["body"]
    assert data.userId == payload["userId"]


@pytest.mark.parametrize(
        "post_id", 
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
def test_update_post(api_client, payload, post_id):
    """полностью обновить пост"""
    response = api_client.put(f"/posts/{post_id}", json=payload)
    assert response.status_code == 200

    data = PostSchema(**response.json())

    assert data.id == post_id
    assert data.title == payload["title"]
    assert data.body == payload["body"]
    

@pytest.mark.parametrize(
        "post_id", 
        [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    )
def test_partial_update_post(api_client, post_id):
    """частично обновить пост"""
    response = api_client.patch(f"/posts/{post_id}", json={"title": "Новый заголовок"})
    assert response.status_code == 200

    data = PostSchema(**response.json())

    assert data.id == post_id
    assert data.title == "Новый заголовок"


@pytest.mark.parametrize(
        "post_id", 
        [5, 12, 27, 43, 56, 61, 78, 82, 90, 99]
    )
def test_delete_post(api_client, post_id):
    """удалить пост"""
    response = api_client.delete(f"/posts/{post_id}")

    assert response.status_code == 200
    assert response.json() == {}


