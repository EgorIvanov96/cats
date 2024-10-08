# Проект: Котята API

Добро пожаловать в проект **Котята API**! Этот проект предоставляет RESTful API для управления пользователями, породами котят и самими котятами.

## Описание

API позволяет пользователям:
- Регистрироваться и аутентифицироваться.
- Создавать, обновлять и удалять записи о котятах.
- Получать список доступных пород котят.

## Установка

Чтобы запустить проект на своем локальном компьютере, следуй следующим шагам:

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/EgorIvanov96/cats
   cd cats-api
   ```

2. Создай и активируй виртуальную среду:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте: venv\Scripts\activate
   ```

3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Поменяйте в settings.py DATABASES:
   ```DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'django_user',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'localhost',
        'PORT': '5432'
    }
   ```


5. Примените миграции:
   ```bash
   python manage.py migrate
   ```

6. Запусти сервер:
   ```bash
   python manage.py runserver
   ```

ADMIN:
```
   email - admin@gmail.com
   пароль - admin
   ```


## Запуск через Docker:
Чтобы запустить проект на своем локальном компьютере, следуй следующим шагам:

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/EgorIvanov96/cats
   cd cats-api
   ```

2. Запустите docker-compose.yml
   ```bash
   docker compose up --build
   ```

## Swagger документация:
```
   http://127.0.0.1:8000/swagger/
   ```
## Использование

### Эндпоинты API

- **Пользователи**
  - `POST /api/users/` - Регистрация нового пользователя.
  - `GET /api/users/` - Получение списка пользователей.

- **Породы**
  - `GET /api/porode/` - Получение списка пород котят.

- **Котята**
  - `POST /api/cats/` - Создание нового котенка.
  - `GET /api/cats/` - Получение списка котят.
  - `PUT /api/cats/{id}/` - Обновление информации о котенке.
  - `DELETE /api/cats/{id}/` - Удаление котенка.
  - `GET api/cats/?breed={id}/` - Фильтр по породе котят.

### Примеры запросов

#### Регистрация нового пользователя

```bash
POST http://localhost:8000/api/users/
{
    "email": "1@gmail.com",
    "username": "432",
    "password": "Qw11sasc22"
}
```

#### Получение списка пород

```bash
GET http://localhost:8000/api/porode/
```

#### Создание нового котенка

```bash
POST http://localhost:8000/api/cats/
{
    "porode_cats": 4,
    "cat_name": "Рыжик",
    "color_cat": "черный",
    "years": 6
}
```

