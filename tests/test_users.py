import pytest
from models.user import UserSchema
from utils.assertions import assert_list_not_empty, assert_status_code
import allure


@allure.title("Получить список пользователей")
def test_get_all_users(api_client):
    """получить список всех пользователей"""

    with allure.step("Отправить GET /users"):
        response = api_client.get("/users")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):   
        for user in response.json():
            UserSchema(**user)


@allure.title("Получить пользователя по ID")
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_get_user_by_id(api_client, user_id):
    """получить пользователя по ID"""

    with allure.step("Отправить GET /users/{user_id}"):   
        response = api_client.get(f"/users/{user_id}")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)
        
    with allure.step("Проверить статус код 200"):   
        assert_status_code(response, 200)

    with allure.step("Валидировать ответ"):   
        user = UserSchema(**response.json())
        assert user.id == user_id
