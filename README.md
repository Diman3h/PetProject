# PetProject
Веб-приложение для учета и контроля выполнения задач отдела информационной безопасности. Позволяет фиксировать и отслеживать прогресс выполнения различных метрик ИБ.
## Демонстрация работы

[Видео демонстрация](https://gifyu.com/image/bbpP4)
![image](https://github.com/user-attachments/assets/eb9eb7e2-33e2-40fb-a87a-eb3e8f0fba12)
![image](https://github.com/user-attachments/assets/0a59b618-3dac-451f-a4bd-eed3c84baafb)

## Установка

1. Клонировать репозиторий
2. Создать виртуальное окружение: python -m venv venv
3. Активировать окружение: venv\Scripts\activate
4. Установить зависимости: pip install -r requirements.txt
5. Создать файл `.env` с параметрами подключения к БД
6. Инициализировать БД: python init_db.py
7. Запустить: python flask_app.py

## UPDATE Установка через Docker
1. В терминале с dockerfile запустить
   docker-compose up -d
2. Во втором терминале инициализировать базу данных:
   docker-compose exec web python init_db.py

После установки сайт будет доступен по адресу: http://localhost:5000

Данные для входа(генерируется в init_db.py):
- Логин: admin, Пароль: admin
  
## Стек

- Backend: Python/Flask
- База данных: MySQL
- Frontend: HTML, CSS, JavaScript (jQuery)
- Аутентификация: Flask-Login

## Требования

- Python 3.x
- MySQL Server

## Структура проекта

- `flask_app.py` - основной файл приложения
- `init_db.py` - скрипт инициализации базы данных
- `form_config.py` - примерный базовый файл метрик
- `templates/` - HTML шаблоны для страниц
- `static/` - статические css файлы

