import pytest
from models.comment import CommentSchema


def test_get_comments(api_client):
    """получить список всех комментариев"""

    response = api_client.get("/comments")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for comment in response.json():
        CommentSchema(**comment)


@pytest.mark.parametrize(
        "post_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_comments_for_post(api_client, post_id):
    """получить комментарии для поста"""

    response = api_client.get(f"/comments?postId={post_id}")
    assert response.status_code == 200
    assert len(response.json()) > 0

    for comment in response.json():
        CommentSchema(**comment)