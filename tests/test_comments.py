import pytest
from models.comment import CommentSchema
from utils.assertions import assert_status_code, assert_list_not_empty


def test_get_comments(api_client):
    """получить список всех комментариев"""

    response = api_client.get("/comments")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    for comment in response.json():
        CommentSchema(**comment)


@pytest.mark.parametrize(
        "post_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_comments_for_post(api_client, post_id):
    """получить комментарии для поста"""

    response = api_client.get(f"/comments?postId={post_id}")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    for comment in response.json():
        CommentSchema(**comment)