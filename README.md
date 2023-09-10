# Бронирование переговорок

Проект, который позволяет управлять комнатами и их бронированием.

## Технологический стек

* FastAPI
* FastApiUsers
* Pydantic
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

## Запуск

Чтобы запустить проект, выполните следующую команду:

```
uvicorn app.main:app --reload
```

Для заполнения env, руководствуйтесь следующим примером:

```
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=yoursecret
FIRST_SUPERUSER_EMAIL=user@example.com
FIRST_SUPERUSER_PASSWORD=string
```

## Использование

Для использования проекта ознакомьтесь с документацией, перейдя по адресу: `127.0.0.1:8000/docs`

## Авторы:
- [Vakauskas Vitas](https://github.com/Qerced)
