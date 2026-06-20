# API Test Framework

Автоматизированный фреймворк для тестирования REST API [JSONPlaceholder](https://jsonplaceholder.typicode.com).

## Стек технологий

- **Python 3.12**
- **pytest** — фреймворк для тестов
- **requests** — HTTP клиент
- **pydantic** — валидация схем ответов
- **allure-pytest** — генерация отчётов
- **Docker** — контейнеризация

## Структура проекта

```
api-test-framework/
├── .github/
│   └── workflows/
│       └── tests.yml
├── clients/
│   └── api_client.py
├── models/
│   ├── user.py
│   ├── post.py
│   ├── comment.py
│   ├── todo.py
│   ├── album.py
│   └── photo.py
├── tests/
│   ├── conftest.py
│   ├── test_users.py
│   ├── test_posts.py
│   ├── test_comments.py
│   ├── test_todos.py
│   ├── test_albums.py
│   ├── test_photos.py
│   └── test_negative.py
├── utils/
│   └── assertions.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Покрытие

| Эндпоинт | GET | POST | PUT | PATCH | DELETE |
|---|---|---|---|---|---|
| /posts | ✅ | ✅ | ✅ | ✅ | ✅ |
| /users | ✅ | — | — | — | — |
| /comments | ✅ | — | — | — | — |
| /todos | ✅ | — | — | — | — |
| /albums | ✅ | — | — | — | — |
| /photos | ✅ | — | — | — | — |

Также покрыты негативные сценарии: 404, невалидные данные, несуществующие эндпоинты.

## Запуск локально

```bash
pip install -r requirements.txt
pytest -v --alluredir=allure-results
allure serve allure-results
```

## Запуск через Docker

```bash
docker compose run --rm tests
```

## Allure отчёт

Актуальный отчёт доступен после каждого прогона CI:

🔗 https://allkery.github.io/API-test-framework/

## CI/CD

Тесты запускаются автоматически при каждом пуше в `main` и при открытии Pull Request. После прогона Allure отчёт деплоится на GitHub Pages.