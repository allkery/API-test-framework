import pytest
from models.photo import PhotoSchema
from utils.assertions import assert_list_not_empty, assert_status_code
import allure


@allure.title("Получить список фотографий")
def test_get_photos(api_client):
    """получить список всех фотографий"""

    with allure.step("Отправить GET /photos"):
        response = api_client.get("/photos")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for photo in response.json():
            PhotoSchema(**photo)


@allure.title("Получить фотографию по айди")
@pytest.mark.parametrize(
        "photo_id",
        [234, 456, 678, 789, 890, 901, 912, 923, 934, 945]
    )
def test_get_photo_by_id(api_client, photo_id):
    """получить фотографию по ID"""

    with allure.step("Отправить GET /photos/{photo_id}"):
        response = api_client.get(f"/photos/{photo_id}")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        validated = PhotoSchema(**response.json())
        assert validated.id == photo_id