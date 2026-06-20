import pytest
from models.user import UserSchema
from utils.assertions import assert_list_not_empty, assert_status_code


def test_get_all_users(api_client):
    """получитить список всех пользователей"""
    
    response = api_client.get("/users")

    assert_status_code(response, 200)
    assert_list_not_empty(response)


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_get_user_by_id(api_client, user_id):
    """получить пользователя по ID"""

    response = api_client.get(f"/users/{user_id}")
    user = UserSchema(**response.json())

    assert_status_code(response, 200)
    assert user.id == user_id