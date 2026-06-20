import pytest
from models.todo import TodoSchema
from utils.assertions import assert_list_not_empty, assert_status_code


def test_get_todos(api_client):
    """получить список всех задач"""

    response = api_client.get("/todos")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    for todo in response.json():
        TodoSchema(**todo)


@pytest.mark.parametrize(
        "user_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_todos_by_user_id(api_client, user_id):
    """получить список всех задач пользователя"""

    response = api_client.get(f"/users/{user_id}/todos")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    for todo in response.json():
        validated = TodoSchema(**todo)
        assert validated.userId == user_id


@pytest.mark.parametrize(
        "todo_id",
        [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    )
def test_get_todo_by_id(api_client, todo_id):
    """получить задачу по ее ID"""

    response = api_client.get(f"/todos/{todo_id}")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    validated = TodoSchema(**response.json())
    assert validated.id == todo_id