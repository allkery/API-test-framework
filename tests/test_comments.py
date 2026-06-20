import pytest
from models.comment import CommentSchema
from utils.assertions import assert_status_code, assert_list_not_empty
import allure


@allure.title("Получить список комментариев")
def test_get_comments(api_client):
    """получить список всех комментариев"""

    with allure.step("Отправить GET /comments"):
        response = api_client.get("/comments")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)
        
    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for comment in response.json():
            CommentSchema(**comment)


@allure.title("Получить комментарии для поста")
@pytest.mark.parametrize(
        "post_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_comments_for_post(api_client, post_id):
    """получить комментарии для поста"""

    with allure.step(f"Отправить GET /comments?postId={post_id}"):
        response = api_client.get(f"/comments?postId={post_id}")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 200"):
        assert_status_code(response, 200)

    with allure.step("Проверить, что список не пуст"):
        assert_list_not_empty(response)

    with allure.step("Валидировать элементы ответа"):
        for comment in response.json():
            CommentSchema(**comment)