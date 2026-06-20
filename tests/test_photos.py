import pytest
from models.photo import PhotoSchema
from utils.assertions import assert_list_not_empty, assert_status_code


def test_get_photos(api_client):
    """получить список всех фотографий"""

    response = api_client.get("/photos")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    for photo in response.json():
        PhotoSchema(**photo)


@pytest.mark.parametrize(
        "photo_id",
        [234, 456, 678, 789, 890, 901, 912, 923, 934, 945]
    )
def test_get_photo_by_id(api_client, photo_id):
    """получить фотографию по ID"""

    response = api_client.get(f"/photos/{photo_id}")

    assert_status_code(response, 200)
    assert_list_not_empty(response)

    validated = PhotoSchema(**response.json())
    assert validated.id == photo_id