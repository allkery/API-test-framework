import pytest
from models.todo import TodoSchema
from utils.assertions import assert_list_not_empty, assert_status_code
import allure


@allure.title("Получить список задач")
def test_get_todos(api_client):
    """получить список всех задач"""

    with allure.step("Отправить GET /todos"):
        response = api_client.get("/todos")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for todo in response.json():
            TodoSchema(**todo)


@allure.title("Получить список задач пользователя")
@pytest.mark.parametrize(
        "user_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_todos_by_user_id(api_client, user_id):
    """получить список всех задач пользователя"""

    with allure.step("Отправить GET /users/{user_id}/todos"):
        response = api_client.get(f"/users/{user_id}/todos")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for todo in response.json():
            validated = TodoSchema(**todo)
            assert validated.userId == user_id


@allure.title("Получить задачу по айди")
@pytest.mark.parametrize(
        "todo_id",
        [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    )
def test_get_todo_by_id(api_client, todo_id):
    """получить задачу по ее ID"""

    with allure.step("Отправить GET /todos/{todo_id}"):
        response = api_client.get(f"/todos/{todo_id}")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элемент ответа"):
        validated = TodoSchema(**response.json())
        assert validated.id == todo_id