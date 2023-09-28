# Бронирование переговорок

Сервис бронирования помещений на определённый период времени.

## Технологический стек

* FastAPI
* FastApiUsers
* Pydantic
* Aiogoogle
* SQLAlchemy
* Alembic
* SQLite
* Uvicorn

## Установка

Чтобы установить проект, выполните следующие команды:

```
git clone git@github.com:Qerced/room_reservation.git
cd room_reservation
pip install -r requirements.txt
```

## Настройка

В проекте уже существуют готовые миграции, которые вы можете применить для работы базы данных:

```
alembic upgrade head
```

Для заполнения env, необходимо получить [JSON-файл](https://cloud.google.com/iam/docs/keys-create-delete) с ключом доступа к сервисному аккаунту. Руководствуйтесь следующим примером для корректной работы всего проекта:

```
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=yoursecret
FIRST_SUPERUSER_EMAIL=user@example.com
FIRST_SUPERUSER_PASSWORD=PASSWORD
TYPE=service_account
PROJECT_ID=PROJECT_ID
PRIVATE_KEY_ID=KEY_ID
PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n
CLIENT_EMAIL=SERVICE_ACCOUNT_EMAIL
CLIENT_ID=CLIENT_ID
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL
EMAIL_USER=creator_service@example.com
```

## Запуск

Чтобы запустить проект, выполните следующую команду:

```
uvicorn app.main:app --reload
```

## API

Чтобы узнать больше о методах, реализованных в проекте, перейдите на страницу документации [Swagger](http://127.0.0.1:8000/docs) или [ReDoc](http://127.0.0.1:8000/redoc).

## Авторы:
- [Vakauskas Vitas](https://github.com/Qerced)
