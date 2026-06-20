import pytest
from models.album import AlbumSchema
from models.photo import PhotoSchema


def test_get_albums(api_client):
    """получить список всех альбомов"""

    response = api_client.get("/albums")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for album in response.json():
        AlbumSchema(**album)


@pytest.mark.parametrize(
        "album_id",
        [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    )
def test_get_album_by_id(api_client, album_id):
    """получить альбом по его ID"""

    response = api_client.get(f"/albums/{album_id}")

    assert response.status_code == 200
    assert len(response.json()) > 0

    validated = AlbumSchema(**response.json())
    assert validated.id == album_id


@pytest.mark.parametrize(
        "user_id",
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
def test_get_albums_by_user_id(api_client, user_id):
    """получить список всех альбомов пользователя"""

    response = api_client.get(f"/users/{user_id}/albums")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for album in response.json():
        validated = AlbumSchema(**album)
        assert validated.userId == user_id


@pytest.mark.parametrize(
        "album_id",
        [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    )
def test_get_photos_for_album(api_client, album_id):
    """получить список всех фотографий альбома"""

    response = api_client.get(f"/albums/{album_id}/photos")

    assert response.status_code == 200
    assert len(response.json()) > 0

    for photo in response.json():
        PhotoSchema(**photo)