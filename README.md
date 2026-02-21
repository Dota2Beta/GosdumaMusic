# GosdumaMusic (Django)

## Быстрый запуск (PyCharm / terminal)

1. Создайте и активируйте виртуальное окружение:
   - Windows: `python -m venv .venv && .venv\\Scripts\\activate`
   - Linux/macOS: `python -m venv .venv && source .venv/bin/activate`
2. Установите зависимости:
   - `pip install -r requirements.txt`
3. Примените миграции:
   - `python manage.py migrate`
4. Запустите проект:
   - `python manage.py runserver`

## Если ошибка: `ModuleNotFoundError: No module named 'django'`

Это означает, что Django не установлен в выбранном интерпретаторе.

Исправление:
1. В PyCharm выберите правильный Python Interpreter (желательно из `.venv`).
2. Выполните `pip install -r requirements.txt`.
3. Повторите запуск `python manage.py runserver`.

## Доступ администратора

- Логин: `BraveGuap`
- Пароль: `gosdum`

Пользователь создается миграцией `portal/migrations/0002_create_default_admin.py`.
