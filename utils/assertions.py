def assert_status_code(response, expected_code=200):
    assert response.status_code == expected_code

def assert_list_not_empty(response):
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0