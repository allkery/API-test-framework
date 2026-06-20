import pytest
from models.album import AlbumSchema
from models.photo import PhotoSchema
from utils.assertions import assert_list_not_empty, assert_status_code
import allure


@allure.title("Получить список альбомов")
def test_get_albums(api_client):
    """получить список всех альбомов"""

    with allure.step("Отправить GET /albums"):
        response = api_client.get("/albums")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for album in response.json():
            AlbumSchema(**album)


@allure.title("Получить альбом по айди")
@pytest.mark.parametrize(
        "album_id",
        [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    )
def test_get_album_by_id(api_client, album_id):
    """получить альбом по его ID"""

    with allure.step("Отправить GET /albums/{album_id}"):
        response = api_client.get(f"/albums/{album_id}")
        allure.attach(response.text, name="Response body",
                attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        validated = AlbumSchema(**response.json())
        assert validated.id == album_id


@allure.title("Получчить список всех альбомов пользователя")
@pytest.mark.parametrize(
        "user_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_albums_by_user_id(api_client, user_id):
    """получить список всех альбомов пользователя"""

    with allure.step("Отправить GET /users/{user_id}/albums"):
        response = api_client.get(f"/users/{user_id}/albums")

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for album in response.json():
            validated = AlbumSchema(**album)
            assert validated.userId == user_id


@allure.title("получить список всех фотографий альбома")
@pytest.mark.parametrize(
        "album_id",
        [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    )
def test_get_photos_for_album(api_client, album_id):
    """получить список всех фотографий альбома"""

    with allure.step("Отправить GET /albums/{album_id}/photos"):
        response = api_client.get(f"/albums/{album_id}/photos")

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for photo in response.json():
            PhotoSchema(**photo)