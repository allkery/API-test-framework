import allure


@allure.title("Получить несуществующий пост")
def test_get_non_existent_post(api_client):
    """получить несуществующий пост"""

    with allure.step("Отправить GET /posts/9999"):
        response = api_client.get("/posts/9999")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 404"):
        assert response.status_code == 404


@allure.title("Получить несуществующий пользователь")
def test_get_non_existent_users(api_client):
    """получить несуществующий пользователь"""

    with allure.step("Отправить GET /users/9999"):
        response = api_client.get("/users/9999")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 404"):
        assert response.status_code == 404


@allure.title("Получить несуществующую задачу")
def test_get_non_existent_todo(api_client):
    """получить несуществующую задачу"""

    with allure.step("Отправить GET /todos/9999"):
        response = api_client.get("/todos/9999")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 404"):
        assert response.status_code == 404


@allure.title("Получить несуществующий эндпоинт")
def test_get_non_existent_endpoint(api_client):
    """получить несуществующий эндпоинт"""

    with allure.step("Отправить GET /nonexistent"):
        response = api_client.get("/nonexistent")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 404"):
        assert response.status_code == 404


@allure.title("Создать пост с невалидными данными")
def test_create_post_with_invalid_data(api_client):
    """создать пост с невалидными данными"""
    """
    jsonplaceholder не валидириует тело запроса,
    поэтому возвращает 201, а не 400
    """

    payload = {
        "title": 123,  # должно быть строкой
        "body": True,  # должно быть строкой
        "userId": "abc"  # должно быть числом
    }

    with allure.step("Отправить POST /posts с невалидными данными"):
        response = api_client.post("/posts", json=payload)
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 201"):
        assert response.status_code == 201


@allure.title("Создать пост без данных")
def test_create_post_without_payload(api_client):
    """создать пост без данных"""
    """
    jsonplaceholder не валидириует тело запроса,
    поэтому возвращает 201, а не 400
    """

    with allure.step("Отправить POST /posts без данных"):
        response = api_client.post("/posts")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 201"):
        assert response.status_code == 201


@allure.title("Получить пост с строковым ID")
def test_get_post_with_string_id(api_client):
    """получить пост с строковым ID"""

    with allure.step("Отправить GET /posts/abc"):
        response = api_client.get("/posts/abc")
        allure.attach(response.text, name="Response body",
            attachment_type=allure.attachment_type.JSON)

    with allure.step("Проверить статус код 404"):
        assert response.status_code == 404