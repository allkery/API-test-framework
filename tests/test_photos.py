import pytest
from models.photo import PhotoSchema


def test_get_photos(api_client):
    """получить список всех фотографий"""

    response = api_client.get("/photos")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for photo in response.json():
        PhotoSchema(**photo)


@pytest.mark.parametrize(
        "photo_id",
        [234, 456, 678, 789, 890, 901, 912, 923, 934, 945]
    )
def test_get_photo_by_id(api_client, photo_id):
    """получить фотографию по ID"""

    response = api_client.get(f"/photos/{photo_id}")

    assert response.status_code == 200
    assert len(response.json()) > 0

    validated = PhotoSchema(**response.json())
    assert validated.id == photo_id