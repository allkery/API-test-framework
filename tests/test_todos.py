import pytest
from models.todo import TodoSchema


def test_get_todos(api_client):
    """получить список всех задач"""

    response = api_client.get("/todos")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for todo in response.json():
        TodoSchema(**todo)


@pytest.mark.parametrize(
        "user_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_todos_by_user_id(api_client, user_id):
    """получить список всех задач пользователя"""

    response = api_client.get(f"/users/{user_id}/todos")

    assert response.status_code == 200
    assert len(response.json()) > 0

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

    assert response.status_code == 200
    assert len(response.json()) > 0

    validated = TodoSchema(**response.json())
    assert validated.id == todo_id