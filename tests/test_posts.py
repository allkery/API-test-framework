from models.post import PostSchema
import pytest
from utils.assertions import assert_status_code, assert_list_not_empty
import allure


@allure.title("Получить список всех постов")
def test_get_posts(api_client):
    """получить список всех постов"""

    with allure.step("Отправить GET /posts"):
        response = api_client.get("/posts")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for post in response.json():
            PostSchema(**post)


@allure.title("Получить список всех постов пользователя")
@pytest.mark.parametrize(
        "user_id", 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_posts_by_user_id(api_client, user_id):
    """получить список всех постов пользователя"""

    with allure.step("Отправить GET /users/{user_id}/posts"):
        response = api_client.get(f"/users/{user_id}/posts")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for post in response.json():
            validated = PostSchema(**post)
            assert validated.userId == user_id


@allure.title("Получить пост по айди")
@pytest.mark.parametrize(
        "post_id",
        [5, 12, 27, 43, 56, 61, 78, 82, 90, 99]
    )
def test_get_post_by_id(api_client, post_id):
    """получить пост по его ID"""
    with allure.step("Отправить GET /posts/{post_id}"):
        response = api_client.get(f"/posts/{post_id}")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Валидировать ответ"):
        post = PostSchema(**response.json())
        assert post.id == post_id


@allure.title("Создать новый пост")
def test_create_post(api_client, payload):
    """создать пост"""

    with allure.step("Отправить POST /posts"):
        response = api_client.post("/posts", json=payload)
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 201"):
        assert_status_code(response, 201)

    with allure.step("Валидировать ответ"):
        data = PostSchema(**response.json())

        assert data.id == 101
        assert data.title == payload["title"]
        assert data.body == payload["body"]
        assert data.userId == payload["userId"]


@allure.title("Обновить пост")
@pytest.mark.parametrize(
        "post_id", 
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    )
def test_update_post(api_client, payload, post_id):
    """полностью обновить пост"""
    with allure.step("Отправить PUT /posts/{post_id}"):
        response = api_client.put(f"/posts/{post_id}", json=payload)
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Валидировать ответ"):
        data = PostSchema(**response.json())

        assert data.id == post_id
        assert data.title == payload["title"]
        assert data.body == payload["body"]
        assert data.userId == payload["userId"]


@allure.title("Частично обновить пост")
@pytest.mark.parametrize(
        "post_id", 
        [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    )
def test_partial_update_post(api_client, post_id):
    """частично обновить пост"""

    with allure.step("Отправить PATCH /posts/{post_id}"):
        response = api_client.patch(f"/posts/{post_id}", json={"title": "Новый заголовок"})
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Валидировать ответ"):
        data = PostSchema(**response.json())

        assert data.id == post_id
        assert data.title == "Новый заголовок"


@allure.title("Удалить пост")
@pytest.mark.parametrize(
        "post_id", 
        [5, 12, 27, 43, 56, 61, 78, 82, 90, 99]
    )
def test_delete_post(api_client, post_id):
    """удалить пост"""
    with allure.step("Отправить DELETE /posts/{post_id}"):
        response = api_client.delete(f"/posts/{post_id}")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Валидировать ответ"):
        assert response.json() == {}


